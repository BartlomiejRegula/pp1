class Student():
    id=10000
    szkola='Uek krakow'
    def __init__(self,name,surname,kierunek):
        self.name=name
        self.surname=surname
        self.id=Student.id
        Student.id+=1
        self.kierunek=kierunek


    def __str__(self):
        return f'{self.name} {self.surname} ({self.id}), {self.kierunek},{Student.szkola}'

m=Student('Anna', 'MAJ', 'Applied Informatics')
print(m)
m=Student('aaa', 'bbb', 'Applied Informatics')
print(m)
m=Student('aaaa', 'bbbb', 'Applied Informatics')
print(m)
