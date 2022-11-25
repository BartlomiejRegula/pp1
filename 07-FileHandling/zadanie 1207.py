file=open('lista.txt','a',encoding='UTF-8')

for i in range(3):
    file.write(input('dodaj produkt '))
    file.write('\n')


file.close()