def gcd(m,n):
    if m==0:
        return n
    elif n==0:
        return m
    else:
        return gcd(n%m,m)


n = int(input())
for i in range(n):
    a,b = map(int,input().split(" "))
    c_stack = gcd(a,b)
    print(c_stack,end="\n")
