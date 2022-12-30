def f1(a):
    parz=0
    x=[]
    for i in a:
        if i%2==0:
            parz=i
            if parz>8:
                x.append(parz)
    return len(x)





print(f1([13,7,4,16,3,12,8]))

