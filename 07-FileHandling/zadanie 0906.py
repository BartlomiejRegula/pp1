file=open('numbers.txt','r')

x=0
for line in file:
    x=x+int(line)
print(x)


file.close()