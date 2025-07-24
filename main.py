import os
import requests
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from openai import OpenAI
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

load_dotenv(override=True)

api_key = os.getenv('OPENAI_API_KEY')
openai = OpenAI(api_key=api_key)
headers = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

# Flask app setup
app = Flask(__name__)
CORS(app)

class Website:
    def __init__(self, url):
        """Create this Website object from the given url using the BeautifulSoup library please :)"""
        self.url = url
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup.body(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.body.get_text(separator="\n", strip=True)

system_prompt = "You are an assistant that analyzes the contents of a website \
and provides a short summary, ignoring text that might be navigation related. \
Respond in markdown. Use emojis and make it fun and engaging :)"

def user_prompt_for(website):
    user_prompt = f"You are looking at a website titled {website.title}"
    user_prompt += "\nThe contents of this website is as follows; \
    please provide a short summary of this website in markdown. \
    If it includes news or announcements, then summarize these too.\n\n \
    use emojis and make it fun and engaging"
    user_prompt += website.text
    return user_prompt

def messages_for(website):
    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt_for(website)}
    ]

def summarize_for_api(url):
    try:
        website = Website(url)
        response = openai.chat.completions.create(
            model = "gpt-4o-mini",
            messages = messages_for(website)
        )
        return {
            "success": True,
            "title": website.title,
            "url": url,
            "summary": response.choices[0].message.content
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

# Flask routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({"success": False, "error": "URL is required"}), 400
    
    result = summarize_for_api(url)
    return jsonify(result)


if __name__ == '__main__':    
    print("🚀 Starting What Kinda Website Is This server...")
    print("📱 Open your browser to: http://localhost:8000")
    app.run(debug=True, host='0.0.0.0', port=8000)