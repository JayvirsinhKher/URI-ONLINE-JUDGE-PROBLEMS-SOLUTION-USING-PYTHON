
while True:
    p1,p2 = input().split(" ")
    p1,p2=int(p1),int(p2)
    if(p1==0 or p2==0):
        break
    elif(p1 > 0 and p2 > 0):
        print('primeiro',end="\n")
    elif(p1 > 0 and p2 < 0):
        print('quarto',end="\n")
    elif(p1 < 0 and p2 < 0):
        print('terceiro',end="\n")
    else:
        print('segundo',end="\n")

