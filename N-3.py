import re
patt = "[a-z]+_[a-z]*"
if re.search(patt, input()):
    print("T")
else:
    print("F")