def f(first_letter,last_letter):
    import re
    with open('test.txt','r',encoding='UTF-8') as file:
        a=file.readlines()
        znajdz = re.findall(rf'\b[{first_letter}]\w+\w+[{last_letter}]\b', str(a), re.I)
    
    
    return len(znajdz)





print(f("w", "d") )