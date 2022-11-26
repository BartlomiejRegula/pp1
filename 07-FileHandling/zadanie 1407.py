file=open(input('podaj nazwe pliku: '),'r',encoding='UTF-8')


x=0
for i in file:
    x=x+1
print('liczba linii:',x)


file.close()
