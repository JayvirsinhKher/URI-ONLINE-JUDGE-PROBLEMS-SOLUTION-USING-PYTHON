
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

pos = 0
neg = 0

if(a>0):
    pos+=1
if(b>0):
    pos+=1
if(c>0):
    pos+=1
if(d>0):
    pos+=1
if(e>0):
    pos+=1
if(f>0):
    pos+=1

print(pos,"valores positivos",end="\n")
