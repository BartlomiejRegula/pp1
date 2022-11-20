a=[1,2,3,4,5,6,7,8]

even=[]
odd=[]


for i in a:
    if i%2==0:
        even.append(i)
        a.remove(i)

a2=[1,2,3,4,5,6,7,8]

for i in a2:
    if i%2!=0:
         odd.append(i)
         a2.remove(i)
print(even)
print(odd)

