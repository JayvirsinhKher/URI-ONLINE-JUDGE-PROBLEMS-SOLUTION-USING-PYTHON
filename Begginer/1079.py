
n = int(input())

a = list()
b = list()
c = list()

avg = list()

for i in range(n):
    j,k,l= input().split(" ")
    a.append(float(j))
    b.append(float(k))
    c.append(float(l))

    avg.append((a[i]*2 + b[i]*3 + c[i]*5)/10)

for i in range(n):
    print("%0.1f"%avg[i],end="\n")


        
    
        


