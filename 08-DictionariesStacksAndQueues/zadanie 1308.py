student_data={
    'name':'bartek',
    'age': 18,
    'adult': True
}
import json
with open('student.json','w') as file:
    json.dump(student_data,file,ensure_ascii=False,indent=4)
