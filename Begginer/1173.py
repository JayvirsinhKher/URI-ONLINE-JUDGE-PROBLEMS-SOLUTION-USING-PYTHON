x = list()
n = int(input())
if n<50:
    for k in range(0,10):
        x.append(n)
        n *=2
        print("N[%d]"%k,"=","%d"%x[k],end="\n")
    
