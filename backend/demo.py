# # import tweepy
# # import os
# # from dotenv import load_dotenv

# # # Load environment variables
# # load_dotenv()

# # # Authenticate with OAuth 2.0 Bearer Token
# # client = tweepy.Client(
# #     bearer_token=os.getenv("TWITTER_BEARER_TOKEN"),
# #     consumer_key=os.getenv("TWITTER_API_KEY"),
# #     consumer_secret=os.getenv("TWITTER_API_SECRET"),
# #     access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
# #     access_token_secret=os.getenv("TWITTER_ACCESS_SECRET")
# # )

# # try:
# #     response = client.create_tweet(text="🚀 Hello, Twitter API!")
# #     print("✅ Tweet posted successfully:", response)
# # except tweepy.TweepyException as e:
# #     print("❌ Error:", e)

# import tweepy
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# # Authenticate with OAuth 1.0a (needed for media uploads)
# auth = tweepy.OAuth1UserHandler(
#     consumer_key=os.getenv("TWITTER_API_KEY"),
#     consumer_secret=os.getenv("TWITTER_API_SECRET"),
#     access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
#     access_token_secret=os.getenv("TWITTER_ACCESS_SECRET")
# )

# api = tweepy.API(auth, wait_on_rate_limit=True)

# try:
#     # Upload an image
#     media = api.media_upload("test.jpg")  # Replace with your image file
#     print("✅ Image uploaded successfully:", media.media_id)

#     # Post tweet with media
#      response = client.create_tweet(text="🚀 Hello, Twitter API!")
#      print("✅ Tweet posted successfully:", response)
#     tweet_text = "🚀 Tweeting with an image! #TwitterAPI"
#     api.update_status(status=tweet_text, media_ids=[media.media_id])
#     print("✅ Tweet posted successfully!")

# except tweepy.TweepyException as e:
#     print("❌ Error:", e)
# from google import genai
# import os
# import re
# from dotenv import load_dotenv

# # Load API Key
# load_dotenv()
# GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# # Initialize Gemini Client
# client = genai.Client(api_key=GEMINI_API_KEY)

# def extract_problem_name(extracted_text):
#     """
#     Extract the problem name from text using regex and pattern recognition.
#     """
#     # Look for a known structure (problem title appearing before "Difficulty:")
#     match = re.search(r"([\w\s\-]+)(?=\s*Difficulty:)", extracted_text, re.IGNORECASE)

#     if match:
#         problem_name = match.group(1).strip()
#         return problem_name

#     # If regex fails, use fallback: Find first meaningful title in text
#     lines = extracted_text.split("\n")
#     for line in lines:
#         if "Difficulty" in line:
#             return line.split("Difficulty")[0].strip()

#     return "Unknown Problem"

# def generate_tweet(problem_name, streak_day):
#     """
#     Uses Gemini API to generate a structured and meaningful tweet.
#     """
#     try:
#         prompt = f"""
#         You are a helpful AI that generates Twitter posts for coding challenges.

#         - The tweet should be **engaging, motivational, and under 280 characters**.
#         - Include the **problem name** correctly in a natural way.
#         - Mention that it's part of the **GFG 160 coding challenge**.
#         - Use hashtags like: #100DaysOfCode, #geekstreak2025
#         - Mention @geeksforgeeks.

#         **Problem Name:** {problem_name}  
#         **Day:** {streak_day}  

#         Generate a tweet that sounds inspiring and tech-focused!
#         """

#         response = client.models.generate_content(
#             model="gemini-2.0-flash", contents=prompt
#         )

#         return response.text.strip() if response.text else "Failed to generate tweet"

#     except Exception as e:
#         return f"❌ Error: {str(e)}"

# # Example Usage
# extracted_text = """</> Problem B Editorial © Submissions © Comments Python3 +

# a

# 2~ # node class:
# 3

# 4~ class Node:

# Remove loop in Linked List Bd

# Difficulty: Medium Accuracy: 27.66%  Submissions:507K+ —Points:4 Average Time: 45m

# 5° def _ init__(self,val):
# 6 self .next=None
# . . . . 7 self .data=val
# Given the head of a linked list that may contain a loop. A loop means that the last node of 8
# the linked list is connected back to a node in the same list. The task is to remove the loop 10
# i ict (if # j 11~ class Solution:
# from the linked list (if it exists). 12 #Function to remove a loop in the linked list.
# Be def removeLoop(self, head):

# Custom Input format: # code here

# A head of a singly linked list and a pos (1-based index) which denotes the position of the

# } Driver Code Ends
# node to which the last node points to. If pos = 0, it means the last node points to null,

# indicating there is no loop.

# The generated output will be true if there is no loop in list and other nodes in the list remain

# unchanged, otherwise, false.

# Examples:

# Input: head = 1 -> 3 -> 4, pos = 2
# Output: true
# Explanation: The linked list looks like

# a
# """
# problem_name = extract_problem_name(extracted_text)
# streak_day = 1

# # Generate Tweet
# tweet = generate_tweet(problem_name, streak_day)
# print("\n✅ **Generated Tweet:**")
# print(tweet)



# Local JSON file to store streak data
data_file = "streak_data.json"

def load_streak_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return {"last_date": None, "streak": 0}