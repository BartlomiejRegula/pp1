suma=0
ilosc=0
najwieksza=None
najmniejsza=None
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
    if najwieksza is None or y>najwieksza:
        najwieksza=y
    if najmniejsza is None or y<najmniejsza:
        najmniejsza=y
print(f'lacznie liczb:{ilosc}')
print(f'suma liczb:{suma}')
print(f'najwieksza liczba:{najwieksza}')
print(f'najmniejsza liczba:{najmniejsza}')