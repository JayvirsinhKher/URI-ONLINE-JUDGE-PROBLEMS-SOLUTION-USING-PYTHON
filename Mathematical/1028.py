n = int(input())
for i in range(n):
    a,b = map(int,input().split(" "))
    smaller = a if a<b else b
    c_stack = 1
    for j in range(smaller,0,-2):
        if a%j==0 and b%j==0:
            c_stack = j
            break
    print(c_stack,end="\n")
