def f(player1,player2):
    talia={
        'A': 10,
        'K': 10,
        'Q': 10,
        'J': 10,
        'T': 10,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
    }

    wynik1=0
    wynik2=0
    for i in player1:
        if i in talia:
            wynik1+=talia[i]
    for i in player2:
        if i in talia:
            wynik2+=talia[i]
    if wynik1>wynik2:
        return True
    else:
        return False       

print(f("AJ972","AQT72")) 
print(f("9532","K8"))
print(f("987","AT4"))

    # x=0
    # y=0
    # for i in player1:
    #     if i in talia:
    #         x=x+talia[i]
    # for i in player2:
    #     if i in talia:
    #         y=y+talia[i]
    
    # if x>y:
    #     return True
    # else:
    #     return False
    