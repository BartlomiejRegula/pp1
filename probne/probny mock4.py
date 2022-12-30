def f4(d):

    sum=0
    for i,v in d.items():
        for j in v:
            if j >=5 and j <=10:
                sum+=j
    return sum



print(f4({  "arr1":[2,6,5], 
            "arr2":[7,1], 
            "arr3":[2,9,8,1]}))

