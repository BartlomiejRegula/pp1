text = 'X-DSPAM-Confidence: 0.8475'
atpos= text.find(':')
host=float(text[atpos+1:])
print(host)