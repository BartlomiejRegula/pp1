def compare(array1, array2):
    if array1==array2:
        return True
    else:
        return False

a=["water","book","sky"]
b=["water","book","sky"]
c=[True,False]
d=[True,False,True]

print('array1',a)
print('array2',b)
if compare(a,b) == True:
    print('sa takie same')
