par = list()
impar = list()
pa = 0
impa = 0
patrip = 0
impatrip = 0
for i in range(15):
    n = int(input())
    if n%2==0:
        if pa<5 and patrip==0:
            par.append(n)
            pa+=1
        else:
            par[pa] = n
            pa+=1
            
        if pa==5:
            for j in range(5):
                print("par[%d]"%j,"=","%d"%par[j],end="\n")
            pa = 0
            patrip +=1
            
                
    else:
        if impa<5 and impatrip==0:
            impar.append(n)
            impa+=1
        else:
            impar[impa] = n
            impa+=1
            
        if impa==5:
            for j in range(5):
                print("impar[%d]"%j,"=","%d"%impar[j],end="\n")
            impa = 0
            impatrip +=1


for i in range(impa):
    print("impar[%d]"%i,"=","%d"%impar[i],end="\n")
for i in range(pa):
    print("par[%d]"%i,"=","%d"%par[i],end="\n")
        
    
        
