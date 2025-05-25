import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

def list_gemini_models():
    if not GEMINI_API_KEY:
        print("[Gemini] API key not set.")
        return
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        models = genai.list_models()
        print("Available Gemini models:")
        for m in models:
            print(f"- {m.name}")
    except Exception as e:
        print(f"[Gemini] Error: {str(e)}")

def gemini_answer(prompt: str) -> str:
    if not GEMINI_API_KEY:
        return "[Gemini] API key not set."
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
        response = model.generate_content([prompt])
        # The response object may have different attributes depending on the API version
        if hasattr(response, 'text') and response.text:
            return response.text.strip()
        elif hasattr(response, 'candidates') and response.candidates:
            # Fallback for older/newer API versions
            return response.candidates[0].content.parts[0].text.strip()
        else:
            return "[Gemini] No response generated."
    except Exception as e:
        return f"[Gemini] Error: {str(e)}"
