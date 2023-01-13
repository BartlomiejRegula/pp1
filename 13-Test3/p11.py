def f(n):
    x=''
    for i in range(n):
        if i%5!=0 or i==0:
            x+='/' 
        else:
            x+='-/'

    return x




print(f(-7),'1')
print(f(0),'2')
print(f(5))
print(f(7))
print(f(6),'6')
print(f(10))
print(f(11))

