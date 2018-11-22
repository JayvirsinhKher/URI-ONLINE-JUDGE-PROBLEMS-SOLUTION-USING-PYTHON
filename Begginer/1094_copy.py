n = int(input())
total = 0
r = 0
c = 0
s = 0

for i in range(n):
    inp = input().split()
    no, typee = inp
    total += int(no)
    
    if(typee == "C"):
        c += int(no)
    else:
        if(typee == "R"):
            r += int(no)
        else:
            s += int(no)

print("Total: %d cobaias" %total,end="\n")
print("Total de coelhos: %d" %c,end="\n")
print("Total de ratos: %d" %r,end="\n")
print("Total de sapos: %d" %s,end="\n")
print("Percentual de coelhos: {:.2f} %".format((c/float(total))*100),end="\n")
print("Percentual de ratos: {:.2f} %".format((r/float(total))*100),end="\n")
print("Percentual de sapos: {:.2f} %".format((s/float(total))*100),end="\n")
