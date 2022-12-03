import json
with open('limited.json','w') as file, open('students.json','r') as orgfile:
    studenci=json.load(orgfile)
    for i in studenci:
        file.write(i['first_name'])
        file.write(' ')
        file.write(i['last_name'])
        file.write(' ')
        file.write(str(i['id']))
        file.write(' ')
        file.write('\n')
