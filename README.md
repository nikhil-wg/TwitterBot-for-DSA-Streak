# TwitterBot for DSA Streak

## 📌 Overview
TwitterBot for DSA Streak is a web application designed to help developers and competitive programmers track their daily problem-solving streak on platforms like GeeksforGeeks. The bot extracts problem details from uploaded images, maintains a streak counter, and automatically generates and posts tweets to Twitter.

## 🎯 Features
- 🖼️ **Extract Problem Name**: Uses OCR (Tesseract) and AI (Gemini API) to extract the problem name from uploaded images.
- 🔥 **Track Daily Streaks**: Keeps track of the number of consecutive days a user has solved problems.
- 🐦 **Auto-Generate Tweets**: Uses AI to generate engaging tweets about the solved problem.
- 📤 **Post to Twitter**: Automatically uploads the image and tweet to Twitter.
- 🌐 **React Frontend + FastAPI Backend**: A seamless integration of React.js and FastAPI for efficient processing.

---

## 🏆 Who Can Use This Application?
This application is perfect for:
- **Competitive Programmers** 🏁 who want to share their daily problem-solving streaks on Twitter.
- **Coding Enthusiasts** 👨‍💻👩‍💻 who wish to build consistency in their coding habits.
- **Students & Developers** 📚 who participate in daily coding challenges and want an automated way to track and share progress.

---

## 🛠️ Tech Stack
- **Frontend**: React.js (Vite)
- **Backend**: FastAPI (Python)
- **OCR**: Pytesseract
- **AI Model**: Gemini API
- **Database**: JSON-based local storage (for streak tracking)
- **Twitter API**: Tweepy for posting tweets

---

## 🚀 Setup & Installation
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/nikhil-wg/TwitterBot-for-DSA-Streak.git
cd TwitterBot-for-DSA-Streak
```

### **2️⃣ Backend Setup (FastAPI)**
#### Install Dependencies
```sh
cd backend  # Navigate to backend directory
pip install -r requirements.txt
```
#### Configure Environment Variables
Create a `.env` file in the backend folder and add your API keys:
```ini
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_SECRET=your_twitter_access_secret
TWITTER_BEARER_TOKEN=your_twitter_bearer_token
GEMINI_API_KEY=your_gemini_api_key
```
#### Run the Backend Server
```sh
uvicorn main:app --reload
```
The FastAPI backend will run at `http://127.0.0.1:8000`

---

### **3️⃣ Frontend Setup (React.js)**
#### Install Dependencies
```sh
cd frontend  # Navigate to frontend directory
npm install
```
#### Run the Frontend Server
```sh
npm run dev
```
The frontend will be available at `http://localhost:5173`

---

## 📡 Hosting the Application
### **Backend Deployment**
- You can deploy the FastAPI backend for free on **Render, Railway, or Deta Space**.
- Example for **Render**:
  1. Create a new **Web Service** on [Render](https://render.com/).
  2. Connect your GitHub repo and deploy.
  3. Add environment variables under `Settings > Environment`.
  4. Set the **Start Command** to:
     ```sh
     uvicorn main:app --host 0.0.0.0 --port 10000
     ```

### **Frontend Deployment**
- You can deploy the frontend on **Vercel or Netlify** for free.
- Example for **Vercel**:
  1. Install Vercel CLI: `npm install -g vercel`
  2. Deploy: `vercel`
  3. Follow the CLI prompts to complete deployment.

---

## 🎯 Usage
1. **Upload an image** of a solved problem from GeeksforGeeks.
2. The backend extracts the **problem name** and updates your **streak count**.
3. AI generates an **engaging tweet** with hashtags.
4. The app **automatically posts** the tweet and the image to Twitter.

---

🌟 **Star this repo if you like it!** ⭐

