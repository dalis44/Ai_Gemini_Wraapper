# uv run main.py "How do I build a calculator app?" --verbose  role
#.venv\Scripts\activate
#python calculator/tests.py
import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from functions.get_files_info import schema_get_files_info
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from functions.get_file_content import schema_get_file_content
from call_function import call_function
from prompts import system_prompt
MAX_ITERS = 20
def parse_arguments():
    """Parse command-line arguments."""
    load_dotenv("apikey.env")

    verbose = "--verbose" in sys.argv
    # -------Collect all non-flag args as the user prompt-------
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]
    print(args)
    if not args:
        print("AI Code Assistant")
        print('\nUsage: uv run main.py "your prompt here" [--verbose]')
        print('Example: uv run main.py "How do I build a calculator app?"')
        sys.exit(1)

    user_prompt = " ".join(args)
    return user_prompt, verbose
   

def build_messages(user_prompt):
    """Create a Gemini-compatible list of messages (conversation)."""
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)])
    ]

    return messages
  
def generate_content(client, messages, verbose):
    """Send messages to Gemini and print the response."""

    available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_write_file,   
        schema_run_python_file,
        schema_get_file_content,
    ])

    config_GC = types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt)

    
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-001",
            contents=messages,
            config= config_GC,
        )
    except Exception as e:
        print(" Error generating content:", e)
        sys.exit(1)
    
    
    if verbose:
        print(f"User prompt: {messages[0].parts[0].text}")
        print(" Prompt tokens:", response.usage_metadata.prompt_token_count)
        print(" Response tokens:", response.usage_metadata.candidates_token_count)
    
    if response.candidates:
        for candidate in response.candidates:
            function_call_content = candidate.content
            messages.append(function_call_content)

    if not response.function_calls:
        return response.text


    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")
    #print(function_responses)
    messages.append(types.Content(role="user", parts=function_responses))


def main():
    user_prompt, verbose = parse_arguments()

    api_key = os.getenv("GEMINI_API_KEY")
    #api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")

    client = genai.Client(api_key=api_key)
    messages = build_messages(user_prompt)

    iters = 0
    while True:
        iters += 1
        if iters > MAX_ITERS:
            print(f"Maximum iterations ({MAX_ITERS}) reached.")
            sys.exit(1)

        try:
            final_response = generate_content(client, messages, verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")
    #generate_content(client, messages, verbose)


if __name__ == "__main__":
    # Dacă nu sunt argumente, folosește un prompt implicit
    if len(sys.argv) == 1:
        #sys.argv.extend(["what files are in the pkg directory? ", "--verbose"])
        sys.argv.extend(["what is in test.py ? ", "--verbose"])
    
    main() 