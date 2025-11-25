from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test():
  working_directory = "."
  result = get_files_info(working_directory = working_directory, directory = ".")
  print("The output of root directory is : ")
  print(result)
  print("")

  result = get_files_info(working_directory = working_directory, directory = "pkg")
  print("The output of 'pkg' directory is : ")
  print(result)
  print("")  


  result = get_file_content(working_directory = working_directory, file_path = "main.py")
  print(result)

  result = get_file_content(working_directory = working_directory, file_path = "pkg/calculator.py")
  print(result)

  result = write_file(working_directory = working_directory, file_path = "text.txt", content = "my info")
  print(result)

  result = write_file(working_directory = working_directory, file_path = "pkg2/text.txt" , content = "my info")
  print(result)

  result = run_python_file(working_directory = working_directory, file_path = "main.py", args = ["3 + 5"])
  print(result)

if __name__ == "__main__":
    test()