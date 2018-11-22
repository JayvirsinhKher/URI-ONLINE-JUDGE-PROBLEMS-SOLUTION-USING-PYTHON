
x = int(input())
if x>1 and x<1000:
    for i in range(1,x+1):
        a = 1
        while a!=3:
            if a==1:
                print(i,i**2,i**3,end="\n")
                a+=1
            else:
                print(i,i**2+1,i**3+1,end="\n")
                a+=1
        
