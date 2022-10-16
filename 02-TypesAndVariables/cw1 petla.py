suma=0
ilosc=0
while True:
    zbior=input('podaj liczbe:')
    if zbior=='gotowe':
        break
    try:
        y=int(zbior)
    except:
        print('złe dane')
        continue
    ilosc=ilosc+1
    suma=suma+y
    srednia=suma/ilosc
print(f'lacznie liczb:{ilosc}')
print(f'suma liczb:{suma}')
print(f'srednia liczb:{srednia}')