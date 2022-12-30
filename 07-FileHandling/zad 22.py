import csv
with open('students.txt','r') as file:
    f=csv.reader(file)
    x=0
    for i in f:
        print(i[0],'    ', i[1],'   ', i[-1])