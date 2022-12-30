import re
tekst='To be, or not to be, that is the question'
vov=re.findall('[eyuioa]',tekst)
print(len(vov))