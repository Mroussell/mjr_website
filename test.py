import os
import openai
from dotenv import load_dotenv

# Load your API key from an environment variable or secret management service
load_dotenv()
openai.api_key = os.getenv('OPEN_AI_SEC_KEY')

response = openai.Completion.create(engine="text-davinci-002", prompt="Say this is a test", temperature=0, max_tokens=6)