def pcheck(m):
    flag = 0
    for i in range(2,m):
        if m%i==0:
            flag = 1
            break
    if flag==0:
        print(m,"eh primo",end="\n")
    else:
        print(m,"nao eh primo",end="\n")

n = int(input())
for i in range(n):
    x = int(input())
    pcheck(x)
