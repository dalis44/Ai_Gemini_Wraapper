from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test():
  result = get_files_info(r"D:\AWORK\wrapper\calculator",".")
  print("The output of root directory is : ")
  print(result)
  print("")

  result = get_files_info(r"D:\AWORK\wrapper\calculator","pkg")
  print("The output of 'pkg' directory is : ")
  print(result)
  print("")  


  #result = get_files_info(r"D:\AWORK\wrapper\calculator", "../")
  #print("Result for '../' directory:")
  #print(result)

  result = get_file_content(r"D:\AWORK\wrapper\calculator", "main.py")
  print(result)

  result = get_file_content(r"D:\AWORK\wrapper\calculator", "pkg/calculator.py")
  print(result)

  result = write_file(r"D:\AWORK\wrapper\calculator", "text.txt", "my info")
  print(result)

  result = write_file(r"D:\AWORK\wrapper\calculator", "pkg2/text.txt" , "my info")
  print(result)

  result = run_python_file(r"D:\AWORK\wrapper\calculator" , "main.py",["3 + 5"])

if __name__ == "__main__":
    test()