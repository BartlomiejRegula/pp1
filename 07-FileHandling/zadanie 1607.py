with open('countries.txt','r') as file1, open ('copy.txt','a')as file2:
    file1_content=file1.read()
    file2.write(file1_content)
