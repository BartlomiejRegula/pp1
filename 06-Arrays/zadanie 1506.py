# An array contains values: [[0,0,0],[0,0,0],[0,0,0]].
# Create a program that replaces the values of the main diagonal with 1. Use loop statements.
# Display the modified array as below:
# 1 0 0
# 0 1 0
# 0 0 1



a=[ [0,0,0],
    [0,0,0],
    [0,0,0] ]

x=0
y=0
for i in range(0,len(a)):
    # for y in range(0,2):
    if a[x][y]==0:
        a[x][y]=1
    x=x+1
    y=y+1

print(a[0])
print(a[1])
print(a[2])