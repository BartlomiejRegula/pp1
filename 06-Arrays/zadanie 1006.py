a=[1,2,3,4,5,6,7]

p=0
q=0
for i in a:
    if a[p]%2==0:
        print('even',end=' ')
    p+=1
    if a[q]%2!=0:
        print('odd',end=' ')    
    q+=1