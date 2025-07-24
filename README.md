# 🦜 Page Parrot

> **"Squawk! This page says..."**  
Your personal website-summarizing parrot, here to chirp out the essence of any URL in seconds.

---

## 🎉 What is Page Parrot?

**Page Parrot** is a fun little web app that visits a website, pecks through the fluff, and squawks back a delightful, emoji-filled summary powered by **GPT-4o-mini**. Perfect for when you don’t want to read *everything* but still want to know *something*.

---

## 🛠️ Features

✨ **Magical summarizing powers** via OpenAI  
🌍 Just drop a URL — no plugins, no fuss  
🧽 Cleans out scripts, styles, and visual noise  
📝 Returns a concise, markdown-formatted summary  
🎈 Uses emojis to make it fun and readable  
📦 Simple API and cute frontend

---

## 📦 Tech Stack

- 🐍 Python + Flask  
- 🤖 OpenAI (GPT-4o-mini)  
- 🧼 BeautifulSoup4 for page cleaning  
- 🌐 Flask-CORS  
- 🎭 dotenv for config  
- 🔮 HTML templates for fun!

---

## 🚀 How to Run It

1. Clone this birdcage:
   ```bash
   git clone https://github.com/your-username/page-parrot.git
   cd page-parrot
   ```

2. Install the squawk requirements:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key in a `.env` file:
   ```ini
   OPENAI_API_KEY=your-api-key-here
   ```

4. Start the parrot server:
   ```bash
   python app.py
   ```

5. Open your browser to [http://localhost:8000](http://localhost:8000) and start squawking URLs 🦜
