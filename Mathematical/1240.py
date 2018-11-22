n = int(input())
for i in range(n):
    j,k=map(int,input().split(" "))
    if (j>=1 and j<2**31) and (k>=1 and k<2**31):

        if j%10==k%10 and j>=k:
            print("encaixa",end="\n")
        else:
            print("nao encaixa",end="\n")
