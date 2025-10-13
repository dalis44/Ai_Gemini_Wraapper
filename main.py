import os
from dotenv import load_dotenv
import google.generativeai as genai

def main():
    # Load environment variables
    load_dotenv("apikey.env")

    # Get the Gemini API key
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")

    # Configure the Gemini client
    genai.configure(api_key=api_key)

    # Generate content
    model = genai.GenerativeModel("gemini-2.0-flash-001")
    response = model.generate_content("This is a good way to learn Python AI development")

    # Display token usage and response
    print("Prompt tokens:", response.usage_metadata.prompt_token_count)
    print("Response tokens:", response.usage_metadata.candidates_token_count)
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()