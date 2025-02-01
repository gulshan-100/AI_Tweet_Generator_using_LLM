from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv, find_dotenv
import os

# Load environment variables from .env file
load_dotenv(find_dotenv())

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Initialize the language model for tweet generation
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature =1,
    google_api_key=GEMINI_API_KEY
)
