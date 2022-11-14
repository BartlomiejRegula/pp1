pin=input('Enter the PIN code:')

if pin == '0805':
    print('Correct')
else:
    while pin != "0805":
        if pin == "0805":
            print('Correct')
            break
        print('Incorrect...')
        pin=input('Enter the PIN code:')
        if pin == "0805":
            print('Correct')
            break
        print('Incorrect...')
        pin=input('Enter the PIN code:')
        if pin == "0805":
            print('Correct')
            break
        print('card blocked')
        break