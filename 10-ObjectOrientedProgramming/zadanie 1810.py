selfarr=[12, 6, 9, 4, 17, 37]

for j in range(len(selfarr)):
    for i in range(len(selfarr)-1):
        if selfarr[i]>selfarr[i+1]:
            selfarr[i], selfarr[i+1]=selfarr[i+1], selfarr[i]

print(selfarr)