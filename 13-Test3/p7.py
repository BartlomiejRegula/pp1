class C:
    @staticmethod
    def m1(n):
        x=''
        for i in str(n):
            if int(i)%2==0:
                x+= str(i) 
        return int(x)

    def m2(n):
        x=1
        czyprawda=True
        for i in str(n):
            if int(i)>int(str(n)[x]):
                czyprawda=False
                break
            else:
                czyprawda=True
            x+=1
            if x==int(i):
                break
        if czyprawda==True:
            return True
        else:
            return False

    def m3(n):
        x=0
        ciagznakow=''
        while x<=9:
            if str(x) not in str(n):
                ciagznakow+=str(x)
            x+=1


        return ciagznakow

print(C.m1(4231564)) 
print(C.m1(79381)) 
print(C.m2(125579)) 
print(C.m2(4357879))
print(C.m3(23557))
print(C.m3(1)) 
