def prin():
    global cr
    global cc
    global n
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==cr and j==cc:
                print("X",end="")
            else:
                print("O",end="")
        print("",end="\n")
    print("@",end="\n")
while True:
    n = int(input())
    if n==0:
        break
    if n>=1 and n<=25:
        
        if n%2==1:
            cr = int(n/2) +1
            cc = int(n/2) +1
        else:
            cr = n-int(n/2)
            cc = n-(int(n/2)-1)
        prin()
        tmove = n**2
        op=1
        if n%2==1:
            for i in range(tmove):
                    if op%2==1:
                        for m in range(op):
                            #right
                            if(cr==n and cc==n):
                                break
                            else:                    
                                cc+=1
                                prin()
                 
                        
                        for m in range(op):
                            #up
                            if(cr==n and cc==n):
                                break
                            else:                    
                                cr-=1
                                prin()
                            
                        op+=1
                    else:
                        for m in range(op):
                            #left
                            if(cr==n and cc==n):
                                break
                            else:                    
                                cc-=1
                                prin()
                        for m in range(op):
                            #down
                            if(cr==n and cc==n):
                                break
                            else:                    
                                cr+=1
                                prin()
                                
                        op+=1
        else:
            for i in range(tmove):
                    if op%2==1:
                        for m in range(op):
                            #left
                            if(cr==n and cc==n):
                                break
                            else:                    
                                cc-=1
                                prin()
                 
                        
                        for m in range(op):
                            #down
                            if(cr==n and cc==n):
                                break
                            else:                    
                                cr+=1
                                prin()
                            
                        op+=1
                    else:
                        for m in range(op):
                            #right
                            if(cr==n and cc==n):
                                break
                            else:                    
                                cc+=1
                                prin()
                        for m in range(op):
                            #up
                            if(cr==n and cc==n):
                                break
                            else:                    
                                cr-=1
                                prin()
                                
                        op+=1
            
