class C:
    def __init__(self,stadion):
        self.stadion=stadion
    
    def m1(self,s,n):
        for key,value in self.stadion.items():
            if s== key:
                value+=n
                self.stadion[s]=value
                break
        if s not in self.stadion:
            self.stadion[s]=n
        return self.stadion
        
    def m2(self,a):
        x=0
        for i in a:
            for key, value in self.stadion.items():
                if i==key: 
                    x+=value
        return x



c=C({   'a':120, 
        'D':150,
        'G':90,
        'K':110     })
print(c.m1('G',130))
print(c.m2(['G','D']))
print(c.m2(['K','E','J']))