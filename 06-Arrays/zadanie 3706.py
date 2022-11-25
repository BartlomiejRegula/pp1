arr=[[7, 3, 7, 9, 0],
    [2, 9, 0, 1, 5],
    [3, 8, 6, 4, 7],
    [8, 7, 1, 1, 5]]

x=0
for i in arr[-1]:
    x=x+i
print(x)

x=0
suma=0
for il in arr[x]:
    
    suma+=arr[x][-1]
    x+=1
    if x==3:
        break
print(suma)
