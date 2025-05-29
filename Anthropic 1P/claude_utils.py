# Utility functions to be used in the prompting engineering of Claude
# Avoiding to repeat this section over and over

# Load the API key from the .env file
import os
from dotenv import load_dotenv

def setup_and_load_claude():
    """
    Load the API key from the .env file and set up the model name.
    """
    # Load environment variables from .env file
    load_dotenv('../.env')

    # Get your API key
    api_key = os.getenv('API_KEY')
    if not api_key:
        raise ValueError("API_KEY not found in .env file")

    print(f"API_KEY: {api_key[:10]}...")  # Print first 10 characters for security
    model_name = "claude-3-haiku-20240307"

    # Print the model name
    print(f"MODEL_NAME: {model_name}")

    return api_key, model_name
