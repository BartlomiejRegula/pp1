film_titles=['star wars 1','star wars 2','star wars 3','star wars 4','star wars 5']
file=open('filmy.txt','a',encoding='UTF-8')
for i in film_titles:
    file.write(i)
    file.write('\n')


file.close()