def f1(t):
    import re
    names=re.findall(r'[A-Z][a-z]+',t)
    ages=re.findall(r'\d+',t)
    slownik={}
    for i in range(len(names)):
        slownik[names[i]]=ages[i]
    return dict(sorted(slownik.items()))

def f2(d):
    sum=0
    for i in d.values():
        sum+=int(i)
    return sum





def main():
    print(f1("Mark is 24 and Ann is 27"))
    print(f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!")) 
    print(f2(f1("Mark is 24 and Ann is 27")))
    print(f2(f1("Peter is 11, Barbara is 7 and their grandfather John is 103!!")))

if __name__=='__main__':
    main()
