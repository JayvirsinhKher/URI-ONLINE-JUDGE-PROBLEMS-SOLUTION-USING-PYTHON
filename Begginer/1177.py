t = int(input())
n = list()
if t>=2 and t<=50:
    for i in range(1000):
        n.append(i%t)
    for j in range(1000):
        print("N[%d]"%j,"=","%d"%n[j],end="\n")
