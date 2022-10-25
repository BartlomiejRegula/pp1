from tkinter import E

def abc():
    zdanie='You never get a second chance to make a first impression'
    count=0
    for i in zdanie:
        if i=='e':
            count=count+1
    print(count)
abc()