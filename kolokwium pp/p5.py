class C:
    def __init__(self,imie,nazwisko,wiek,staz):
        self.imie=imie
        self.nazwisko=nazwisko
        self.wiek=wiek
        self.staz=staz

    def __str__(self):
        x=''
        x+=self.imie[0]
        x+=self.nazwisko
        x+=str(self.wiek)
        if self.staz>=5:
            x+='+'
        return x 

print(C('Anna','May',24,7))
print(C('Geore','Brown',32,4))
