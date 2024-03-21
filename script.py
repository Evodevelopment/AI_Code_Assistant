import openai
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def setup_openai_client(api_key):
    """
    Configures the OpenAI client with the given API key.
    """
    openai.api_key = api_key

def get_response_from_openai(prompt, model="gpt-3.5-turbo-instruct"):
    """
    Sends a prompt to the OpenAI API using the specified model and returns the response.
    """
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        temperature=0.7,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Example usage
if __name__ == "__main__":
    setup_openai_client("your_api_key_here")
    prompt = "Write a short story about a robot learning to love."
    response = get_response_from_openai(prompt)
    print(response)
