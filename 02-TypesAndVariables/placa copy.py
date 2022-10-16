godz=float(input('Podaj liczbe godzin:\n'))
stawka=float(input('podaj stawke:\n'))
wyn= godz*stawka
if godz>40:
    x=godz%40
    godz = 40*stawka+x*stawka*1.5
    wyn=godz
    print('wynagrodzenie',wyn)
else:
    print('wynagrodzenie',wyn)
