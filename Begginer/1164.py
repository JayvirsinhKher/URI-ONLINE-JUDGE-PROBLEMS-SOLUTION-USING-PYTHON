def pcheck(m):
    sum1 = 0
    for i in range(1,m):
        if m%i==0:
            sum1 +=i
    if m==sum1:
        print(m,"eh perfeito",end="\n")
    else:
        print(m,"nao eh perfeito",end="\n")

n = int(input())
for i in range(n):
    x = int(input())
    pcheck(x)
