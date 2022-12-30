import re
temp="Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
wynik=re.findall('\d{2}',temp)

sum=0
for i in wynik:
    sum+=int(i)
sr=sum/len(wynik)
print(sr)