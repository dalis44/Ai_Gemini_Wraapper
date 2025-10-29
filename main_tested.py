#.venv\Scripts\activate
#python calculator/tests.py
import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
os.environ["PYTHONUNBUFFERED"] = "1"
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content

def parse_arguments():
    """Parse command-line arguments."""
    
    print((sys.argv))
    prompt = sys.argv[1]
    sys.stdout.flush()
    verbose = "--verbose" in  sys.argv
    if(len(sys.argv) < 2):
         print("I need a prompt @")
         sys.exit(1)
    if(len(sys.argv) == 3 and sys.argv[2]== "--verbose"):
         verbose = True
    prompt = sys.argv[1]



    return prompt , verbose

    
    

def build_mesage(prompt): 
    messages = [types.Content(role ="user" , parts =[types.Part(text = prompt)])]  
    return messages
        
def generate_content(client, messages, verbose):
    try:
        response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents = messages,
                )
    except Exception as e:
         print(" Error generating content:", e)
         sys.exit(1)
             

    print(" Prompt tokens:", response.usage_metadata.prompt_token_count)
    print(" Response tokens:", response.usage_metadata.candidates_token_count)
    print("Usage metadata:", response.usage_metadata)
    print("Reponse")
    print(response.text)
    print("\nResponse:", flush=True)
    print(response.text, flush=True)
     

def main():
    load_dotenv("apikey.env")
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")
    prompt , moreinfo = parse_arguments()
    client = genai.Client(api_key=api_key)
    messages = build_mesage(prompt)
    generate_content(client , messages , moreinfo)
    
    
       
#    main()
if __name__ == "__main__":
        print(get_files_info("calculator",'pkg'))
        print(get_file_content(r"D:\AWORK\wrapper\calculator" , "lorem.txt"))
        main()