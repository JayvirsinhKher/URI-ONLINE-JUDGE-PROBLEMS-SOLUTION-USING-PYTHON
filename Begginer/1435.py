while True:
    n = int(input())
    if(n==0):
        break
    else:
        for i in range(n):
            k=1
            for j in range(n):
                if i==0 or j==0 or i==n-1 or j==n-1:
                    k=1
                    print(k,end=" ")
                else:
                    if i==j:
                        k+=1
                    else:
                        k=i
                    print(k,end=" ")                        
            print("",end="\n")
