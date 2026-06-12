"""LLM Client for Google Gemini API with retry logic."""
#Authentication : API keys and security
#Rate Limiting : API usage quotas and delay
#Network issues : Transient network failures and timeouts
#Response validation : Ensuring valid responses
#Communication layer 
#Exponential backoff : Increasing delay between retries
import time
from google import genai
from config import GEMINI_API_KEY, DEFAULT_MODEL, MAX_RETRIES, RETRY_DELAY
from utils import get_logger

logger = get_logger(__name__)

#You create an LLMClient class that encapsulates the logic for interacting with the Gemini API. The class includes retry logic to handle transient errors and ensure robust communication with the API. The call method sends a prompt to the Gemini API and returns the response, implementing retries with exponential backoff in case of failures.
class LLMClient:
    """Gemini API client"""
    
    def __init__(self, model_name=DEFAULT_MODEL, max_retries=MAX_RETRIES, retry_delay=RETRY_DELAY):
        self.model_name = model_name
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def call(self, prompt: str, **kwargs) -> str:
        """Send prompt to Gemini API"""
        for attempt in range(self.max_retries + 1):
            try:
                response = self.client.models.generate_content(
                    contents=prompt, 
                    model=self.model_name, 
                    **kwargs
                )
                if response and response.text:
                    return response.text.strip()
                else:
                    raise Exception("Empty response received")
                
            except Exception as e:
                if attempt == self.max_retries:
                    raise Exception(f"API call failed after {self.max_retries + 1} attempts: {e}")
                
                time.sleep(self.retry_delay * (2 ** attempt))