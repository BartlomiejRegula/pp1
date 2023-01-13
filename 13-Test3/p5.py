class C:
    def __init__(self,arr):
        self.arr=arr
            

    def __str__(self):
        x=''
        for i in self.arr:
            if i !=self.arr[-1]:
                x+=str(i)+'+'
            else:
                x+=str(i)
        y=sum(self.arr)     
        x+='='+str(y)   
        return x
    
print(C ([5,12]))
print(C([6,0,15]))