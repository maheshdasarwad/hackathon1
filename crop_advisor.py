import os
import google.generativeai as genai
from typing import Optional, Tuple
from dotenv import load_dotenv

load_dotenv()

class CropAdvisor:
    def __init__(self):
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable not found")

        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        self.base_prompt = """You are an agricultural expert..."""  # Keep your original prompt

    def get_crop_advice(self, crop_name: str) -> Tuple[Optional[str], Optional[str]]:
        try:
            if not crop_name.strip():
                return None, "Please enter a valid crop name."

            response = self.model.generate_content(f"{self.base_prompt}{crop_name}")
            return response.text, None

        except Exception as e:
            error_msg = f"AI Error: {str(e)}"
            if "API key" in error_msg.lower():
                error_msg += "\nPlease check your GOOGLE_API_KEY configuration"
            return None, error_msg