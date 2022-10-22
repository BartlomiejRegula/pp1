jeden_zł=int(1)
dwa_zł=int(2)
piec_zł=int(5)
amount=int(input('enter the amount:'))

# [jeden_zł,dwa_zł,piec_zł]

ile5=amount//piec_zł
ile2=ile5//dwa_zł
ile1=ile2//jeden_zł

if ile5*piec_zł == amount:
    print(f'5 zł - {ile5}')
elif ile2*dwa_zł == amount:
    print(f'2 zł - {ile2}')
elif ile1*jeden_zł == amount:
    print(f'1 zł - {ile1}')
elif ile5*piec_zł+dwa_zł == amount:
        print(f'5 zł - {ile5}')
        print(f'2 zł - {ile2}')
elif ile5*piec_zł+dwa_zł+dwa_zł== amount:
        print(f'5 zł - {ile5}')
        print(f'2 zł - {ile2}')
#elif 


else:
    print(f'5 zł - {ile5}')
    print(f'2 zł - {ile2}')
    print(f'1 zł - {ile1}')