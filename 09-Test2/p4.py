def f(dictionary,x,y):
    
    
    wynik=0
    for v,i in dictionary.items():
        for p in i:
            if p >= x and p <= y:
                wynik+=p
    return wynik






print(f({"arr1":[4,5,6],"arr2":[7,5]},  5, 6) )
print(f({"arr1":[2,6,5], "arr2":[7,1], "arr3":[2,9,8,1]}, 5, 10))