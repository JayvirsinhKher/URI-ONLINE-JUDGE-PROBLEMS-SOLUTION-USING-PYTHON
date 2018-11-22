def cal(x1,y1,x2,y2):
    x=list()
    for i in range(1,9):
        for j in range(1,9):
            if x1+i<=8 and y1+i<=8 and x1-i>0 and y1-i>0 and x1>=1 and x1<=8 and y1>=1 and y1<=8:
                x.append((x1+i,y1+i))
                x.append((x1+i,y1-i))
                x.append((x1-i,y1+i))
                x.append((x1-i,y1-i))
                x.append((x1,y1+i))
                x.append((x1,y1-i))
                x.append((x1+i,y1))
                x.append((x1-i,y1))

    print(x)
    print(len(x))

    if (x2,y2) in x:
        print("Present")
    else:
        print("Not Present")
            
            
    
    
while True:
    x1,y1,x2,y2 = map(int,input().split())
    if x1==0 and x2==0 and y1==0 and y2==0:
        break
    else:
        cal(x1,y1,x2,y2)
