import re
with open('grades.txt','r') as file:
    zmienna = re.findall('\d.\d',file.read())
    
    print(zmienna)

    arr=[]
    for i in zmienna:
        arr.append(float(i))
    
    mean=sum(arr)/len(arr)
    print(round(mean,2))