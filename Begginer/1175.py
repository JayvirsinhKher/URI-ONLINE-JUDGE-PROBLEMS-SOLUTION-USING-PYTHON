x = list()
for i in range(20):
    x.append(float(input()))
y = list(x)
ind = -1
for i in range(20):
    y[i] =x[ind]
    ind -=1
        
for k in range(20):
    print("N[%d]"%k,"=","%d"%y[k],end="\n")
    
