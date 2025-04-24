import os
from dotenv import load_dotenv

# Load environment variables from the .env file inside the same directory
def load_env():
    dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(dotenv_path)

def get_serper_api_key():
    load_env()
    return os.getenv("SERPER_API_KEY")

def get_gemini_api_key():
    load_env()
    return os.getenv("GEMINI_API_KEY")

def get_groq_api_key():
    load_env()
    return os.getenv("GROQ_API_KEY")

def get_openrouter_api_key():
    load_env()
    return os.getenv("OPENROUTER_API_KEY")


print("SERPER_API_KEY:", get_serper_api_key())
print("EMINI_API_KEY:", get_gemini_api_key())
print("GROQ_API_KEY:", get_groq_api_key())
print("OPENROUTER_API_KEY:", get_openrouter_api_key())
