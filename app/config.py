import os
from dotenv import load_dotenv

load_dotenv()
class Config:
    API_URI = os.getenv("API_URI")
    CLIENT_ID = os.getenv("CLIENT_ID")