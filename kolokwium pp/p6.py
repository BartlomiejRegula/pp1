class C:
    def __init__(self,tablica):
        self.tablica=tablica
    
    def m(self,a):
        sum=0
        for i in self.tablica:
            if a==i:
                sum+=1
        return sum      

    # m([1,8])
c=C(([8,3],[1,8],[-6,4],[1,8]))
print(c.m([1,8]))
