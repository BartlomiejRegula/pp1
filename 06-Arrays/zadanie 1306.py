a=[[3,9,2],[2,4,5],[7,1,6],[0,4,8]]
parzyste=0
nieparzyste=0

x=0
for i in a[x]:
    if i%2==0:
        parzyste+=i

for i in a[1]:
    if i%2==0:
        parzyste+=i

for i in a[2]:
    if i%2==0:
        parzyste+=i


for i in a[3]:
    if i%2==0:
        parzyste+=i

print(parzyste)