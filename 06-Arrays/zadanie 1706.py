a=[8,2,5,1,9]

x=0
for i in a:
    a[x]=a[x]**2
    x=x+1

print(a)