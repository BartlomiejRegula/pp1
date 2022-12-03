film={
    'tytul':'starwars',
    'rok':'1923',
    'dobry': True,
    'ocena': 10
}   
import json
with open('favourite.json','w') as file:
    json.dump(film,file,ensure_ascii=False,indent=4)
