import os
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
# model = genai.GenerativeModel("models/text-bison-001")
model = genai.GenerativeModel("models/gemini-2.0-flash")

response = model.generate_content("Hello from test script!")
print(response.text)
