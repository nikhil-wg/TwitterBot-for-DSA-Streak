import os
import re
import tweepy
import logging
import pytesseract
import google.generativeai as genai
from fastapi import FastAPI, UploadFile, File
from PIL import Image
from io import BytesIO
import json
from datetime import datetime, timedelta
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from google import genai
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load environment variables
load_dotenv()

# Twitter API credentials
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

# Gemini API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
AIclient = genai.Client(api_key=GEMINI_API_KEY)


# Configure FastAPI app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # React frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Twitter API clients
client = tweepy.Client(
    bearer_token=TWITTER_BEARER_TOKEN,
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_SECRET
)

auth = tweepy.OAuth1UserHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

# Local JSON file to store streak data
data_file = "streak_data.json"

def load_streak_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return {"last_date": None, "streak": 0}

def save_streak_data(data):
    with open(data_file, "w") as file:
        json.dump(data, file) 

def extract_text_from_image(image_bytes):
    image = Image.open(BytesIO(image_bytes))
    return pytesseract.image_to_string(image)

def extract_problem_name(extracted_text):
    try:
        prompt = f"""
        Given the following extracted text from an image, identify the problem name:

        ```text
        {extracted_text}
        ```

        The problem name is usually at the top and followed by details like "Difficulty:", "Accuracy:", or "Submissions:". 
        Return only the problem name without any extra words or symbols.
        """

        response = AIclient.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )
        
        if response and response.text:
            problem_name = response.text.strip()
            return problem_name
        
        return "Unknown Problem"

    except Exception as e:
        logging.error(f"❌ AI Extraction Error: {str(e)}")
        return "Unknown Problem"


def update_streak():
    data = load_streak_data()
    last_date_str = data["last_date"]
    last_date = datetime.strptime(last_date_str, "%Y-%m-%d") if last_date_str else None
    today = datetime.today().date()

    if last_date and last_date == today - timedelta(days=1):
        data["streak"] += 1
    else:
        data["streak"] = 1

    data["last_date"] = str(today)
    save_streak_data(data)
    return data["streak"]

def generate_tweet(problem_name, streak_day):
    try:
        prompt = f"""
        Generate a Twitter post for a coding challenge:
         **Day:** {streak_day}  
        - Keep it under 280 characters.
        - Add \n after each line of the tweet content.
        - Add emojis and tell mover about the problem .
        - problem name: **{problem_name}**.
        - Use hashtags like #gfg160, #geekstreak2025.
        - Mention @geeksforgeeks.

        
        use this format and add \n after each line of the tweet content and add emojis to make the tweet engaging.
        Day: 10 of #gfg160
        problem name: Linked List Cycle
        #geekstreak2025 @geeksforgeeks.

        
        """

        response = AIclient.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )
        generated_tweet = response.text.strip() if response.text else None

        if not generated_tweet:
            logging.error("🚨 AI failed to generate a tweet.")
            return None

        return generated_tweet

    except Exception as e:
        logging.error(f"❌ AI Tweet Generation Error: {str(e)}")
        return None  # Ensures tweet posting won't proceed

@app.post("/upload")
async def upload_image(image: UploadFile = File(...)):
    if not image.filename.lower().endswith((".jpg", ".jpeg", ".png")):
        return {"message": "Invalid file format! Please upload an image file."}

    try:
        logging.info("📸 Image received, starting processing...")

        image_bytes = await image.read()
        extracted_text = extract_text_from_image(image_bytes)
        logging.info(f"🔍 Extracted Text: {extracted_text}")

        problem_name = extract_problem_name(extracted_text)
        logging.info(f"📝 Problem Name: {problem_name}")

        streak_day = update_streak()
        logging.info(f"🔥 Streak updated to {streak_day}")

        # Generate tweet using Gemini AI
        tweet_text = generate_tweet(problem_name, streak_day)

        if not tweet_text:
            return {
                "message": "Tweet generation failed. The tweet was not posted.",
                "streak": streak_day,
                "problem_name": problem_name
            }

        logging.info(f"🐦 Final Tweet: {tweet_text}")

        # Upload image to Twitter
        logging.info("📤 Uploading image to Twitter...")
        image_file = BytesIO(image_bytes)
        media = api.media_upload(filename=image.filename, file=image_file)
        logging.info(f"✅ Image uploaded, media_id: {media.media_id}")

        # Post tweet
        client.create_tweet(text=tweet_text, media_ids=[media.media_id])
        logging.info("✅ Tweet posted successfully!")

        return {
            "message": "Tweet posted successfully!",
            "streak": streak_day,
            "problem_name": problem_name
        }

    except Exception as e:
        logging.error(f"❌ Error: {str(e)}")
        return {"message": f"Error: {str(e)}", "streak": None}
