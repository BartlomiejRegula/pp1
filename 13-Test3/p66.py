class C:
    def __init__(self,ile):
        self.ile=ile
    def m1(self):
        print( self.ile)
    def m2(self):
        self.ile+=1
    def m3(self):
        self.ile-=1
    def m4(self,dodaj):
        self.ile+=dodaj






c=C(5)
c.m1()
c.m2()
c.m1() 
c.m4(-8)
c.m1() 
c.m3()
c.m1() 
c.m4(10)
c.m1() 
