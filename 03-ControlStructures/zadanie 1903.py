try:
    ludzkie_lata=int(input('Enter the dogs age in human years:'))
    if ludzkie_lata<=2:
        print(ludzkie_lata*10.5)
    elif ludzkie_lata>2:
        print(((ludzkie_lata-2)*4)+21)
except:
    print('MUSISZ WPROWADZIĆ LICZBĘ!!!!!!!')