import re
from wsgiref.util import request_uri


def f(c,n):
    
    x=[0,0]
    for i in c:
        if i >= n:
            x[0]+=1
        elif i < n:
            x[1] += 1
    return x

print(f([16],10))
print(f([57,24,77,192,191],100))