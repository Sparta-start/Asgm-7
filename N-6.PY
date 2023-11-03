import re
def colum(a):
    patt = "[ ,.]"
    return re.sub(patt, ":", a)
print(colum(input()))