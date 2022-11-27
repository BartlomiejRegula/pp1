import re
zdanie='To be, or not to be, that is the question'

slowa = re.findall('\w+',zdanie)

print(len((slowa)))