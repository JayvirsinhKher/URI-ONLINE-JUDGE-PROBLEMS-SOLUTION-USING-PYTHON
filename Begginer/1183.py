m = list()
sum1 = 0
avg = 0.0
count = 0

op = input()
for i in range(12):
    col = list()
    for j in range(12):
        col.append(float(input()))
    m.append(col)
        
for j in range(12):
    for k in range(12):
        if j<k:
            sum1 +=m[j][k]
            count+=1
            
if op=="S":
    print("%0.1f"%sum1,end="\n")
elif op=="M":
    avg = sum1/count
    print("%0.1f"%avg,end="\n")
        
