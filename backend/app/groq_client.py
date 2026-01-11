import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key=os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key)

def generate_ai_response(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content
