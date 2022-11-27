import csv
x=[]
with open("students.txt", "r") as file:
    reader = csv.reader(file)


    for i in reader:
        print(i[0],'    ',i[1],'    ',i[-1])


    


