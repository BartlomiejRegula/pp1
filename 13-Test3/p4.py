def f(d):
    arr=[]
    for i in range(len(d)):
        if d[i][1]=='in':
            arr.append(d[i][0])
        if d[i][1]=='out':
            arr.remove(d[i][0])
    return sorted(arr)









cars = [["KR234","in"],["BA123","in"],["GX444","in"],["KR234","out"],
            ["BA111","in"],["BA123","out"],["KR234","in"]]
print(f(cars))