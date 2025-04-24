import os
from langchain.chat_models import ChatOpenAI
from utils import get_gemini_api_key, get_groq_api_key, get_openrouter_api_key  

# Load API keys into env vars
os.environ["GEMINI_API_KEY"] = get_gemini_api_key()
os.environ["GROQ_API_KEY"] = get_groq_api_key()
os.environ["OPENROUTER_API_KEY"] = get_openrouter_api_key()

# Model names
os.environ["GEMINI_MODEL_NAME"] = "gemini-2.0-flash"
os.environ["GROQ_MODEL_NAME"] = "llama-3.3-70b-versatile"
os.environ["OPENROUTER_MODEL_NAME"] = "deepseek/deepseek-chat-v3-0324:free"

# Gemini LLM
gemini_llm = ChatOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta",
    api_key=os.environ["GEMINI_API_KEY"],
    model_name=os.environ["GEMINI_MODEL_NAME"],
    temperature=0.5,
    streaming=True
)

# Groq LLM
groq_llm = ChatOpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.environ["GROQ_API_KEY"],
    model_name=os.environ["GROQ_MODEL_NAME"],
    temperature=0.3,
    streaming=True
)

# OpenRouter LLM
openrouter_llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],
    model_name=os.environ["OPENROUTER_MODEL_NAME"],
    temperature=0.6,
    streaming=True
)
