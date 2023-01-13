from operator import truediv


def f(a):
    import re
    czyprawda=True
    x=re.findall(r'[A-Z]',a)
    x1=re.findall(r'[a-z]',a)
    y=re.findall(r'\d',a)
    if (len(x) == 1 or len(x) == 2) and (len(y) ==1 or len(y)==2 or len(y) ==3 or len(y) == 4) and len(x1)==0:
        czyprawda=True
    else:
        czyprawda=False
    return czyprawda

print(f("G121212"))
print(f("123F"))