def f(w):
    sum=0
    for i in w:
        if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='y') and i !=w[-1]:
            sum += 2
        elif (i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='y') and i ==w[-1]:
            sum+=3
        else:
            sum+=1
    return sum
print(f(''))
print(f('a'))
print(f('because'))