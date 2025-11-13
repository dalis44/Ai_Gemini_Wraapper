import os
import subprocess
# This function  is designed to safely execute a Python script located in a specific working directory and return its output
# ====result -> contains====:
# args =The command that was run
# returncode = Exit code (0 = success, non-zero = error)
# stdout = Captured standard output
# stderr = Captured standard error

#result = subprocess.run(["python", "script.py"], capture_output=True, text=True)
#print(result.returncode)  ---> If script.py runs fine, it returns 0 , otherwise 1
#python main.py "Run the Python script calculator/main.py with arguments ['3 + 5']"

def run_python_file(working_directory, file_path, args= None):
  abs_working_dir = os.path.abspath(working_directory)
  abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
  
  #os.path.commonpath([abs_working_dir, abs_file_path]) == abs_working_dir
  if not abs_file_path.startswith(abs_working_dir):
    return f'Error:  "{file_path}" not readable'
  
  if not os.path.exists(abs_file_path):
    return f'Error: File not found or is not a regular file: "{file_path}"'
  
  if not file_path.endswith(".py"):
    return f'Error: "{file_path}" is not a Python file.'
  
  try:
    commands = ["python", abs_file_path]
    if args:
      commands.extend(args)
    result = subprocess.run(commands,
                            capture_output=True,
                            text=True,
                            timeout=30,
                            cwd = abs_working_dir)
    output = []
    if result.stdout:
      output.append(f"STDOUT:\n{result.stdout}")
    if result.stderr:
      output.append(f"STDERR:\n{result.stderr}")

    if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

    return "\n".join(output) if output else "No output generated"
  
  except Exception as e:
     return f"Error : executing Python file: {e}"
  
#if __name__ == "__main__":
#    print(run_python_file(r"D:\AWORK\wrapper\calculator" , "main.py",["3 + 5"]))
     
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Safely executes a Python script located in the working directory and returns its stdout, stderr, and exit code.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path to the Python file to execute (e.g., 'calculator/main.py')."
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional list of arguments to pass to the script.",
                items=types.Schema(type=types.Type.STRING),
            ),
        },
        required=["file_path"],  # file_path must always be provided
    ),
)
