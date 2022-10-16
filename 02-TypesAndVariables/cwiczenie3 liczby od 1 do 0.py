liczba=float(input('podaj liczbę od 0.0 do 1.0\n'))
if liczba > 1.0:
     print('niepoprawna wartość')
elif liczba >= 0.9:
    print(5,0)
elif liczba >= 0.8:
    print(4.5)
elif liczba >= 0.7:
    print(4,0)
elif liczba >= 0.6:
    print(3.5)
elif liczba >= 0.5:
    print(3,0)
elif liczba < 0.5 and liczba >= 0.0:
    print(2,0)
else:
    print('niepoprawna wartość')