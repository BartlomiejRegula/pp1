ilosc_num=0
sum=0
while True:
    num=int(input('Enter number:'))

    ilosc_num = ilosc_num+1
    sum = sum+num


    if num == 0:
        break
mean = sum/(ilosc_num-1)
print(f'Quantity={ilosc_num-1}, Sum={sum}, Mean={mean}')