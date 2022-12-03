import zadanie_1808 as stack

expr=input('enter expression: ')

x=0
zmienna=[]
for i in expr:
    if i == '1' or '2' or '3' or '4' or '5' or '6' or '7' or '8' or '9' or '0':
        stack.push(i)
        zmienna.append(i)
    elif i == '+' or '-' or '/' or '*':
        stack.pop()
        stack.pop()
        stack.push
    elif i == '=':
        stack.pop()


stack.display()
for i in zmienna:
    print(i,end='')