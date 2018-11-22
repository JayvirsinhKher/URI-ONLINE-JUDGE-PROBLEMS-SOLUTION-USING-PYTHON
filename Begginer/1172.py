x = list()
for i in range(10):
    x.append(int(input()))
    
for j in range(10):
    if x[j]<=0:
        x[j] = 1

for k in range(10):
    print("X[%d]"%k,"=","%d"%x[k],end="\n")
    
