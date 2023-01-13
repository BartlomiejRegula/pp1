class C:
    def __init__(self,liczby):
        self.liczby=liczby

    def __str__(self):
        x=''
        for i in self.liczby:
            if i != self.liczby[-1]:
                x+=str(i)+'+'
            else:
                x+=str(i)
        x+='='+str(sum(self.liczby))
        return x




print(C ([5,12]))
print(C([6,0,15]))
