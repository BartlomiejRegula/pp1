import random
class Arrays():

    @staticmethod
    def dodaj(ile,jaka_liczba):
        arr=[]
        for i in range(ile):
            arr.append(jaka_liczba)
        return arr

    @staticmethod
    def losowe(ile, od, do):
        arr=[]
        for i in range(ile):
            arr.append(random.randrange(od,do))
        return arr

    @staticmethod
    def metoda(array,od,do):
        sum=0
        for i in array:
            if i>=od and i<=do:
                sum+=1
        return sum
            

print(Arrays.dodaj(10,4))
print(Arrays.losowe(10,-7,8))
print(Arrays.metoda([1,2,3,4,5],-1,10))