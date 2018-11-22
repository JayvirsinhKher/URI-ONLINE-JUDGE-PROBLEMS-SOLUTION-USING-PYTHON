x = float(input())
n = [x]
for i in range(1,100):
    n.append(n[i-1]/2.0)
    
for j in range(100):
    print("N[%d]"%j,"=","%0.4f"%n[j],end="\n")
