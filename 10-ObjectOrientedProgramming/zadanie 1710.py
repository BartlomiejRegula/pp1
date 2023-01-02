class Statistic:
    def __init__(self):
        self.arr=[]

    def add(self,dodaj):
        self.arr.append(dodaj)

    def display(self):
        print(*self.arr, sep=' ')
        print(self.arr)


    def big(self):
        print(max(self.arr))
        
    def small(self):
        print(min(self.arr))
    
    def srednia(self):
        x=0
        sum=0
        for i in self.arr:
            sum+=i
            x+=1
        sr=sum/x
        print('sr', sr)
    
    def mediana(self):
        for j in range(len(self.arr)):
            for i in range(len(self.arr)-1):
                if self.arr[i]>self.arr[i+1]:
                    self.arr[i], self.arr[i+1]=self.arr[i+1], self.arr[i]

        if len(self.arr) % 2 == 0:
            print('mediana: ',(self.arr[len(self.arr) // 2 - 1] + self.arr[len(self.arr) // 2]) / 2)
        else:
            print('mediana: ',self.arr[len(self.arr) // 2])
s=Statistic()
s.add(12)
s.add(37)
s.add(6)
s.add(9)
s.add(17)
s.add(21)
s.display()
s.big()
s.small()
s.srednia()
s.mediana()