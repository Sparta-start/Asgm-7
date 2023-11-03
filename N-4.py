import re
def fing(s):
    patt = "[A-Z]+[a-z]*"
    if re.search(patt, s):
        print("T")
    else:
        print("F")
s = input()
fing(s)