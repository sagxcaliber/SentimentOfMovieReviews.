from dotenv import load_dotenv
import os

load_dotenv()


api_key = os.getenv('key')

# cohere model config
model = 'command'
max_token = 10
temperature = 0.3
prompt = ("Analyze the sentiment of the following movie review and classify it as Positive,"
          " Negative, or Neutral:\n\nReview: \"{review}\"\nSentiment:")
