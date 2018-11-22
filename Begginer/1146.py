
def prin(a):
    for i in range(1,a+1):
        if i!=a:
            print(i,end=" ")
        else:
            print(str(i),end="\n")


while True:
    x = int(input())
    if x==0:
        break
    else:
        prin(x)
