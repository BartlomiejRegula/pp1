alphabet={
    'a': 'alpha',
    'b':'beta',
    'r':'romeo',
    't':'tango',
    'k':'kilo',
    'e':'echo'
}

wpis=input('podaj litere: ')

x=0
for i in wpis:
    print(alphabet[i],end=' ')
