
n = int(input())

l = []

for i in range(1,(n+1)):
    l.append(int(input()))

for i in l:
    if (i==0):
        print("NULL",end="\n")
    elif (i%2==0):
        if (i>0):
            print("EVEN POSITIVE")
        else:
            print("EVEN NEGATIVE")
    elif (i%2==1):
        if (i>0):
            print("ODD POSITIVE")
        else:
            print("ODD NEGATIVE")

        
        


