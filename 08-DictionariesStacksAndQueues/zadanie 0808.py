person = {
    "name": "Marek",
    "surname": "Banach",
    "age": 25,
    "hobby": ["swimming","excursions"],
    "married": True,
    "phone":{"landline":"123444321","mobile":"777888999"}
   }

print(person)
print(person['name'])
print(person['hobby'])
person['surname']='nowak'
print(person['surname'])
person['married']=False
print(person['married'])
person['gender']='male'
person['hobby']+=['biking']
person['phone']['work']=6969696969




print(person)
