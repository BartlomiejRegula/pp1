from operator import le


ludzkie_lata=int(input('Enter the dogs age in human years:'))
x=ludzkie_lata/10.5
dog=x+(ludzkie_lata / 4)
if ludzkie_lata <= 21:
    print(x)
elif ludzkie_lata > 21:
    print(dog)