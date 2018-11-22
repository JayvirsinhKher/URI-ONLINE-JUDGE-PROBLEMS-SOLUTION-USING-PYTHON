x = list()
for i in range(100):
    x.append(float(input()))
    
for k in range(100):
    if x[k]<=10:
        print("A[%d]"%k,"=","%0.1f"%x[k],end="\n")
    
