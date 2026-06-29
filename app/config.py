import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_PUBLISHABLE_KEY")
DEVTO_KEY = os.getenv("DEVTO_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
PORT = os.getenv("PORT")
STACKEXCHANGE_KEY = os.getenv("SOF_API_KEY")
WEIGHTS = {
    "github": 60,
    "twitter": 30,
    "website": 20,
    "github_link": 40,
    "email": 50,
    "name": 20,
    "location": 10,
}

MATCH_THRESHOLD = 70