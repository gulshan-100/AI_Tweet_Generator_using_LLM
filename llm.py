from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GEMINI_API_KEY = "AIzaSyA4KBUTVenSp6bESQHqiOAwsW0RS6QLxfM"

# Initialize the language model for tweet generation
llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    temperature=1,
    google_api_key=GEMINI_API_KEY
)
