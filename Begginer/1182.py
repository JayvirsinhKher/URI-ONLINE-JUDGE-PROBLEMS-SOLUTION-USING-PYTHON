m = list()
l = int(input())
sum1 = 0
avg = 0.0
if l>=0 and l<=11:
    op = input()
    for i in range(12):
        col = list()
        for j in range(12):
            col.append(float(input()))
        m.append(col)
        
    for j in range(12):
            sum1 +=m[j][l]
            
    if op=="S":
        print("%0.1f"%sum1,end="\n")
    elif op=="M":
        avg = sum1/12
        print("%0.1f"%avg,end="\n")
        
