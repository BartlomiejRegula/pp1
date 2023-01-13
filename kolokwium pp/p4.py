def f(d,n):
    x=[]
    for key,value in d.items():
        if value > n:
            x.append(key)

    y=''
    for i in x:
        if i!=x[-1]:
            y+=i+','
        else:
            y+=i
    return y

