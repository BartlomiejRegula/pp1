a =  int(input('podaj pierwszy bok\n'))
b =  int(input('podaj drugi bok\n'))
c =  int(input('podaj trzeci bok\n'))

q = a+b+c
s=q/2

pole=(s*(s-a)*(s-b)*(s-c))**0.5

print('pole wynosi\n', pole)