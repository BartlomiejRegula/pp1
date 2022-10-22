suma=0
ilosc=0

while True:
    num=int(input('Enter number:'))
    ilosc=ilosc+1
    suma=suma+num
    if num==0:
        break
srednia=suma/ilosc
print(f'suma:{suma},ilość:{ilosc-1},średnia:{round(srednia,2)}')


