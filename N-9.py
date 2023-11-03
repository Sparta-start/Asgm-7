import re

def splt(N):
    patt = r"[\sA-Z]"
    return re.split(patt, N)

print(" ".join(splt(input())))