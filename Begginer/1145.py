x,y = map(int,input().split(" "))

if (x>1 and x<20) and (x<y and y<100000):
    for i in range(1,y+1):
        if i%x==0:
            print(i,end="\n")
        else:
            print(i,end=" ")
