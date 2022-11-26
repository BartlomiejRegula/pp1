with open('GrainsAndBread.txt','r') as chleb, open('MeatAndFish.txt','r') as mieso, open('shoppinglist.txt','w')  as list:
    list.write(chleb.read())
    list.write(mieso.read())