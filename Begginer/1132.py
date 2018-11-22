x = int(input())
y = int(input())
sum1 = 0
if(x<=y):
    for i in range(x,y+1):
        if(i%13 == 0):
            pass
        else:
            sum1 += i
else:
    for i in range(y,x+1):
        if(i%13 == 0):
            pass
        else:
            sum1 += i
            
print(sum1,end="\n")
