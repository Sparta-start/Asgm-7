import re

def upp(a):
    patt = "[A-Z]"
    return re.split(patt, a)

print(upp(input()))