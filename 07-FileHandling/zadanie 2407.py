import re
zdanie='To be, or not to be, that is the question'
vowels = re.findall('[eayuio]',zdanie)

print(len(vowels))