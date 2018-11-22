

s=0.0
j=0

for i in range(1,40,2):
    s += (i/(2**j))
    j +=1

print("%0.2f"%s,end="\n")
