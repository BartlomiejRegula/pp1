a=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']

longest=len(a[0])
zmienna=a[0]

print('names:')
for i in a:
    print(i, end=' ')
print('')
for i in a:
    if(len(i)>longest):
        longest=len(i)
        zmienna=i
print('max:', zmienna)
