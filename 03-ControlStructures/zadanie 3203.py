for a in range(-1,49,1):
    for b in range(2,49,7):
        print(f'{a+b}',end=' ')
    print()
    if (a+b)>48:
            break