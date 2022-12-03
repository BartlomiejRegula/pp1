import zadanie_1808 as stack
dec=64
zmienna=[]

print(f'wprowadzony numer normalny: {dec}')
while dec!=0:
    stack.push(dec%2)
    zmienna.append(dec%2)
    dec=dec//2
# stack.display()

# zmienna=zmienna[:-1]
# print(zmienna[len(str(zmienna))::-1])
print(f'numer nienormalny: ',end='')

for i in zmienna[len(zmienna)::-1]:
    print(i,end='')

