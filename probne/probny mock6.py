def f6(g,n1,n2):
    import csv
    with open('test.csv','r') as file:
        f=csv.DictReader(file)
        sum=0
        for i in f:
            if i['gender']==g and int(i['children'])>=n1 and int(i['children'])<=n2:
                sum+=1
    return sum


print(f6("Female",2,4))

