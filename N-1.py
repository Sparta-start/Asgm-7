import re 
def match(string):
    pattern = r'a+b*'
    if re.match(pattern, string):
        print("T")
    else:
        print("F")
N = input()
match(N)