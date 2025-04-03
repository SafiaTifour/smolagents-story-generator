import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys and configuration values from environment variables
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
GEMINI_MODEL_ID = os.getenv("GEMINI_MODEL_ID", "gemini/gemini-2.0-flash")  # Default if not set
IMAGE_GEN_TOOL_SPACE = os.getenv("IMAGE_GEN_TOOL_SPACE", "black-forest-labs/FLUX.1-schnell")  # Default if not set
