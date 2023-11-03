import re 
def match(A):
    patt = r'a+bb?'
    if re.match(patt, A):
        print("T")
    else:
        print("F")
b = input()
match(b)