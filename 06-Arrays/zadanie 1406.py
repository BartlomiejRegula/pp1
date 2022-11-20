a=[[True,False],[True,True],[False,False]]

# x=0
tak=True
nie=False

for x in range(0,len(a)):
    for i in range(0,2):
        if a[x][i]==True:
            a[x][i]=False
        elif a[x][i]==False:
            a[x][i]=True  


print(a)