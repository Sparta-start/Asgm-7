import re

def snk(a):
    b = re.split('_', a)
    c = b[0].capitalize()
    d = c + ''.join(word.capitalize() for word in b[1:])
    print(d)
a = input()
snk(a)