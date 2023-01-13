def f(d):
    x=0
    ile=[]
    for i in d:
        if d[x][1]=='in':
            ile.append(i[0])
        if d[x][1]=='out':
            ile.remove(i[0])
        x+=1
    return ile




cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
            ["BA111","in"],["BA123","out"],["KR234","in"]]
print(f(cars))