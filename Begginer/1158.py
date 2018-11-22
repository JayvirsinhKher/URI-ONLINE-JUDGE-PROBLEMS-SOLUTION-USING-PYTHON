
def csum(a,b):
    sum1 = 0
    while b!=0:
        if a%2==0:
            a +=1
        else:
            sum1 +=a
            a +=2
            b -= 1
    print(sum1,end="\n")
n = int(input())
while n!=0:
    x,y=map(int,input().split(" "))
    csum(x,y)
    n -=1
