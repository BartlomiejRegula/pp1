ilosc=input('podaj liczbe monet')
am=int(ilosc)
a=am//5
am%=5
b=am//2
am%=2
print(f'ilosc monet:{ilosc}\n 5zl - {a}\n 2zł - {b}\n 1zł - {am}')