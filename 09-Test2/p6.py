def f(age, course, average) :
    import json
    with open('test.json','r') as file:
        data=json.load(file)
    #     count=0
    #     for i in data:
    #         for j in i['studies']['courses']:
    #             if j['name']==course:
    #                 if sum(j['grades'])/len(j['grades'])>=average and i["age"]>=age:
    #                     count+=1
    # return count
        count=0
        for i in data:
            for j in i['studies']['courses']:
                if j['name']==course:
                    if sum(j['grades'])/len(j['grades'])>=average and i["age"]>=age:
                        count+=1
    return count

print(f(21, "statistics", 4) )