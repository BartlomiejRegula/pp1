class Student():
    id=100000
    szkola='UEK Krakow'
    def __init__(self,name,surname,kierunek):
        self.name=name
        self.surname=surname
        self.kierunek=kierunek
        self.id=Student.id
        Student.id+=1

    def __str__(self):
        return f'{self.name} {self.surname} ({self.id}), {self.kierunek}, {Student.szkola}'

print(Student('anna','maj','informaticks'))
print(Student('aaa', 'bbb', 'Applied Informatics'))
print(Student('aaa', 'bbb', 'Applied Informatics'))
print(Student('aaa', 'bbb', 'Applied Informatics'))
print(Student('aaa', 'bbb', 'Applied Informatics'))
print(Student('aaa', 'bbb', 'Applied Informatics'))
print(Student('aaa', 'bbb', 'Applied Informatics'))
print(Student('aaa', 'bbb', 'Applied Informatics'))
print(Student('aaa', 'bbb', 'Applied Informatics'))
print(Student('aaa', 'bbb', 'Applied Informatics'))
