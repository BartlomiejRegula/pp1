def f5(c):
    import re

    sum=0
    for i in open('test1.txt','r',encoding='UTF-8').readlines():
         if c in i:
            sum+=1
    return sum

print(f5('m'))