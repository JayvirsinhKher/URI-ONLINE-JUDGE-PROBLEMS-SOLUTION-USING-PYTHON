fibo = [0,1]
a = 0
b = 1

for i in range(59):
    c = a+b
    fibo.append(c)
    a,b=b,c


t = int(input())

for i in range(t):
    n = int(input())
    print("Fib(%d)"%n,"=","%d"%fibo[n])
