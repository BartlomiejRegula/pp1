def month(n):
    a=['styczeń','luty','marzec','kwiecien','maj','czerwiec','lipiec','sierpien','wrzesien','pazdziernik','listopad','grudzien']

    if n==1:
        return 'styczeń'
    if n==2:
        return 'luty'
    if n==3:
        return 'marzec'
    if n==4:
        return 'kweicień'
    if n==5:
        return 'maj'
    if n==6:
        return 'czerwiec'
    if n==7:
        return 'lipiec'
    if n==8:
        return 'sierpien'
    if n==9:
        return 'wrzesien'
    if n==10:
        return 'pazdziernik'
    if n==11:
        return 'listopad'
    if n==12:
        return 'grudzien'

print(month(1))