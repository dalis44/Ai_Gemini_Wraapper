
import sys

verbose = "--verbose" in sys.argv

if verbose:
    print("Modul verbose este activat. Se afișează informații detaliate.")
else:
    print("Modul normal. Se afișează doar informațiile esențiale.")

s= "I am glad to finish everything"
ss = ' '.join(s)
print(ss)