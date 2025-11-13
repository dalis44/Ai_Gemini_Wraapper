import os
from google.genai import types
MAX_CHARS = 10000

def get_file_content(working_directory, file_path="."):
  abs_working_dir = os.path.abspath(working_directory)
  abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

  if not abs_file_path.startswith(abs_working_dir):
    return f'Error:  "{file_path}" not readable'
  if not os.path.isfile(abs_file_path):
    return f'Error: File not found or is not a regular file: "{file_path}"'
    
  try:
    with open(abs_file_path, "r") as f:
      content = f.read(MAX_CHARS)
      if os.path.getsize(abs_file_path) > MAX_CHARS:
        content += (f'[...File "{file_path}" truncated at {MAX_CHARS} characters]')
    return content
  except Exception as e:
    return f'Error reading files "{file_path}": {e}'

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a file inside the working directory, returning up to 10,000 characters. Adds a truncation notice if the file is too long.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to the file to read (e.g., 'calculator/lorem.txt')."
            ),
        },
        required=["file_path"],  # file_path must always be provided
    ),
)

#if __name__ == "__main__":
#    print(get_file_content(r"D:\AWORK\wrapper\calculator" , "lorem.txt"))
  
  
  

