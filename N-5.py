import re 

def finic(s):
    patt = "^a.*b$"
    if re.search(patt, s):
        print("T")
    else:
        print("F")
s = input()
finic(s)