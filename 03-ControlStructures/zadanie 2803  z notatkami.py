n1=0    #przypisuje 0 do zmiennej n1
n2=1    #przypisuje 1 do zmiennej n2
count=0 #przypisuje 0 do zmiennej count
while count<50:     #while to pętla która trwa tak długo jak zmienna count jest mniejsza niz 50
    print(n1)       #wyświetla zmienna n1
    nth=n1+n2       #tworzy zmienną nth która zawiera sumę n1 i n2
    n1=n2           #n1 ma od teraz tą wartość co n2
    n2=nth          #n2 ma od teraz tą wartość co nth
    count=count+1   #dodaje 1 do zmiennej count