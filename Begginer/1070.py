
x = int(input())
n = 6
while n!=0:
    if(x%2==1):
        print(x,end="\n")
    else:
        x += 1
        print(x,end="\n")
    x+=2
    n -=1
