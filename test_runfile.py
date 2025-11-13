#from functions.get_files_info import get_files_info
#from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def test():
  

    result = run_python_file(r"D:\AWORK\wrapper\calculator" , "main.py",["3 + 5"])
    print(result)

    result = run_python_file(r"D:\AWORK\wrapper\calculator" , "main.py")
    print("main.py" ,result)

    result = run_python_file(r"D:\AWORK\wrapper\calculator" , "tests.py")
    print("tests.py" ,result)

    result = run_python_file(r"D:\AWORK\wrapper\calculator" , "../main.py")
    print("../main.py" ,result)

    result = run_python_file(r"D:\AWORK\wrapper\calculator" , "nonexistent.py")
    print("nonexistent" , result)

    print("Final try:")
    result = run_python_file(r"D:\AWORK\wrapper\calculator" , "lorem.txt")
    print(result)

if __name__ == "__main__":
    test()