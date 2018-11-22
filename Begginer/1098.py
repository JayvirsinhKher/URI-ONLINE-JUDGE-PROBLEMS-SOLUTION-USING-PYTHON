i = 0
while i<=2:
    i = round(i,1)
    n=1
    while n<=3:
        #print(i)
        if(i==0 or i==1 or i==2):
            print("I=%0.0f"%i,"J=%0.0f"%(n+i),end="\n")
        else:
            print("I=%0.1f"%i,"J=%0.1f"%(n+i),end="\n")
        n += 1
    i += 0.2
     
        


