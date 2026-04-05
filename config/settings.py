"""
Configuration settings for the Sentiment Analysis API
"""
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    """Application settings"""
    
    # API Configuration
    API_TITLE = "Sentiment Analysis API"
    API_DESCRIPTION = "Analyzes text messages to detect sentiment (positive, negative, neutral)"
    API_VERSION = "1.0.0"
    
    # Model Configuration
    MODEL_NAME = "nlptown/bert-base-multilingual-uncased-sentiment"
    LABELS = ["negative", "neutral", "positive"]
    
    # Server Configuration
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", "8000"))
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    # Text Processing
    MAX_TEXT_LENGTH = 512
    MIN_TEXT_LENGTH = 1

settings = Settings()
