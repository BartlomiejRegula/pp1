#Define a function that checks if the number is within the given range <x, y>. 
#The function returns boolean value. Then create a program and use the function you defined
def liczba():
    x=int(input('podaj x:'))
    y=int(input('podaj y:'))
    a=int(input('podaj a:'))
    if (a>=x and a<=y):
        print('jest w przedziale')
    else:
        print('nie jest w przedziale')

liczba()