
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

pos = 0
sump = 0
if(a>=0 or b>=0 or c>=0 or d>=0 or e>=0 or f>=0):
    
    if(a>0):
        pos+=1
        sump +=a
    if(b>0):
        pos+=1
        sump +=b
    if(c>0):
        pos+=1
        sump +=c
    if(d>0):
        pos+=1
        sump +=d
    if(e>0):
        pos+=1
        sump +=e
    if(f>0):
        pos+=1
        sump +=f

print(pos,"valores positivos",end="\n")
print("%0.1f"%(sump/pos),end="\n")
