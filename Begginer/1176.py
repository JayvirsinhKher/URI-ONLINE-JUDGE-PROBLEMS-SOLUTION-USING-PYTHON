def fibo(x):
    a = 0
    b = 1
    m = 0
    c = 0
    if x==0:
        print("Fib (%d)"%x,"=","%d"%a,end="\n")
    elif x==1:
        print("Fib (%d)"%x,"=","%d"%b,end="\n")
        m=1
    else:
        while True:
            if(x==m+1):
                print("Fib(%d)"%x,"=","%d"%c,end="\n")
                break
            else:
                c = a+b
                a,b = b,c
                m +=1

t = int(input())

for i in range(t):
    n = int(input())
    if n>=0 and n<=60:
        fibo(n)
