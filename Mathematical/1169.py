def cal(x):
    sum1 = 0
    j = 1
    for i in range(x-1):
        j*=2
        sum1+=j
        
    ans = int(sum1/12000)
    print("%d"%ans,"kg",end="\n")
    #print(f"{ans} kg",end="\n")
    
n = int(input())
if n>=1 and n<=100:
    for i in range(n):
        x = int(input())
        if x>=1 and x<=64:
            cal(x)


