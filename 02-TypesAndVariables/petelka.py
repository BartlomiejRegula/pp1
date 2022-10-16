suma=0
ilosc=0
while True:
    zbior=input('podaj liczbe')
    if zbior=='gotowe':
        break
    try:
        y=int(zbior)
    except:
        print('zle dane')
        continue
    suma=suma+y
    ilosc=ilosc+1
    srednia=suma/ilosc
print(f'lacznie liczb:{ilosc}')
print(f'suma liczb:{suma}')
print(f'srednia liczb:{srednia}')
