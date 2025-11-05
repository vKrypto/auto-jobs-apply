from openai import OpenAI
import os
from config.logger import logger

openai_client = None

def initialize_openai():
    global openai_client
    if os.getenv("OPENAI_API_KEY"):
        openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        logger.info("OpenAI initialized")
    else:
        logger.warning("OpenAI not configured - using mock AI")

def get_openai():
    return openai_client
