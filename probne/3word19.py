ludzkie = int(input('Enter the dogs age in human years:'))
psie = 0
if ludzkie <= 2:
    psie = ludzkie * 10.5
    print(f'The dogs age in dogs years is {psie} years. ')
elif ludzkie > 2:
    psie = (ludzkie * 4) + 21 - (2*4)
    print(f'The dogs age in dogs years is {psie} years. ')
