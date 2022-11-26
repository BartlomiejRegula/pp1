file=open('linijek30.txt','r',encoding='UTF-8')

x=0
piec=5

for i in file:
    print(i,end='')
    x=x+1
    if x==piec:
        piec=piec+5
        if piec!=35:
            nakliknij=input('wciśnij enter aby kontynuować: ')
        
    
