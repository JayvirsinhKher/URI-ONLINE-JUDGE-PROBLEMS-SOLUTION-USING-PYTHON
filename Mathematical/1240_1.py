import math

def num_digit(m):
    d=0
    while m>0:
        m= int(m/10)
        d+=1
    return d
    
n = int(input())
for i in range(n):
    j,k=map(int,input().split(" "))
    l = num_digit(k)
    l = math.ceil(10**l)
    val = j%l
    if val==k:
        print("encaixa",end="\n")
    else:
        print("nao encaixa",end="\n")
