with open('potegi.txt','w') as filr:
    a=[1,2,3,4,5,6,7,8,9,10]
    y=0
    for i in a:
        x=i
        filr.write(str(x))
        filr.write(' ')
        x=i**2
        filr.write(str(x))
        filr.write(' ')
        x=i**3
        filr.write(str(x))
        filr.write('\n')
        