a=[2, 3, 7, 5, 4]

print(a) #a
print(len(a)) #b
print(a[0]) #c
print(a[1])
print(a[-1])
print(a)
print(a[0]+a[-1])
print(a[2])
for i in a:
    print(i,end=' ')
print()
for i in range(0, int(len(a)/2)+1):
    print(a[i], end=' ')
