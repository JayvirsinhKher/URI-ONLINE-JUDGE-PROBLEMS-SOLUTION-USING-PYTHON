n = int(input())
if n>0 and n<=10**6:
    for i in range(n):
        if i==n-1:
            print("Ho",end="")
        else:
            print("Ho",end=" ")
    print("!",end="\n")
