def f(array2D):

    
    sum=0
    arr=[]
    for i in array2D:
        for j in i:
            sum=sum+i[0]
            break
    arr.append(sum)
        
    sum=0
    for i in array2D:
        for j in i:
            sum=sum+i[1]
            break
    arr.append(sum)

    sum=0
    for i in array2D:
        for j in i:
            sum=sum+i[2]
            break
    arr.append(sum)

    sum=0
    for i in array2D:
        for j in i:
            sum=sum+i[3]
            break
    arr.append(sum)



    return arr
print(f([[3,6,2,7], 
         [9,5,4,0],
         [2,8,0,9]]) )