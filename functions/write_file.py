# python main.py "Create a new file called pkg/readme.txt with the text 'Hello Gemini!'"

import os
from google.genai import types

def write_file(working_directory, file_path, content):
  abs_working_dir = os.path.abspath(working_directory)
  abs_file_path = os.path.abspath(os.path.join(working_directory,file_path))

  if not abs_file_path.startswith(abs_working_dir):
    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
  
  if not os.path.exists(abs_file_path):
    try:
      os.makedirs(os.path.dirname(abs_file_path) , exist_ok = True)
    except Exception as e:
      return f"Error: creating directory: {e}"
         
  if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
    return f'Error: "{file_path}" is a directory, not a file'
  
  try:
      with open(abs_file_path, "w") as f:
        f.write(content)
      return (f'Successfully wrote to "{file_path}" ({len(content)} characters written)') 
  except Exception as e:
      return f"Error: writting to file : {e}" 


from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes text content to a file inside the working directory. Creates directories if they do not exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Relative path to the file to write to (e.g., 'notes/todo.txt')."
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The text content to write into the file."
            ),
        },
        required=["file_path", "content"],
    ),
)
  
     
#write_file("D:\AWORK\wrapper", "calculator/exp.txt", "Nice try")