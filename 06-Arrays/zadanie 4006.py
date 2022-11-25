a=[[-38, 19], 
    [5,40],
    [-7,11],
    [29,16]]

x=0
y=0
for i in range(0,len(a)):
    for j in a[y]:
        if j>=x:
            x=j
    y=y+1

x1=0
y1=0
for i in range(0,len(a)):
    for j in a[y1]:
        if j<=x1:
            x1=j
    y1=y1+1

x2=0
y2=0
for i in a[x2]:
    if x in a[x2]:
        najw= x2
    if x1 in a[x2]: 
        najm= x2
    x2=x2+1
    y2=y2+1

print(x)
print(x1)
print(najw+1)
print(najm+1)