from logging import exception


try:
    godz=float(input('Podaj liczbe godzin:\n'))
    stawka=float(input('podaj stawke:\n'))

    wyn= godz*stawka
    wynx= godz*(stawka*1.5)
    if godz<=40:
        print(wyn)
    elif godz>40:
        print(wynx)
except :
    print('podaj liczbę')