# 20.	Define a function power(x, n) that evaluates xn. Apply recursion. Then calculate 53.
# Tip: xn =  x * xn-1
def power():
    
    x=5
    n=3
    
    print(x*(x**(n-1)))


power()