import random
with open('losowynumer.txt','w') as file:
    for i in random.sample(range(100,999),50):
        file.write(str(i))
        file.write('\n')