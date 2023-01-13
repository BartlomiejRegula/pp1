class C:
    def __init__(self,slownik):
        self.slownik=slownik
    
    def m(self,n):
        x=[]
        for key, value in self.slownik.items():
            if sum(value)/len(value) >=n:
                x.append(key)
        # return x
        x.sort()
        dupa=''
        for i in x:
            if i != x[-1]:
                dupa+=i+','
            else:
                dupa+=i
        return dupa







s = C({ "Peter":[4,5,4],
        "Harry":[2,5], 
        "Barbara":[3,3,3,5,5,5]})
print(s.m(4))
print(s.m(3)) 
print(s.m(5))
