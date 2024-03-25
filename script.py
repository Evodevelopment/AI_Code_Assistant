
import openai
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def setup_openai_client(api_key=None):
    """
    Configures the OpenAI client with the given API key.
    If no API key is provided, attempts to retrieve it from environment variables.
    """
    if api_key is None:
        api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        logging.error("No API key provided or found in environment variables.")
        return False
    openai.api_key = api_key
    return True

def get_response_from_openai(prompt, model="gpt-4-chat", temperature=0.7, max_tokens=150):
    """
    Sends a prompt to the OpenAI API using the specified model and returns the response.
    Includes error handling.
    """
    try:
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].text.strip()
    except Exception as e:
        logging.error(f"Error in getting response from OpenAI: {e}")
        raise

# Example usage
if __name__ == "__main__":
    if setup_openai_client():
        prompt = "Write a short story about a robot learning to love."
        try:
            response = get_response_from_openai(prompt)
            if response:
                print(response)
            else:
                logging.error("Received an empty response from OpenAI.")
        except Exception:
            logging.error("Failed to get a response from OpenAI after retries.")
            
