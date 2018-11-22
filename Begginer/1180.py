n = int(input())
inp = list()
if n>1 and n<1000:
    inp =[int(x) for x in input().split()]

nano = min(inp)
pos = 0
for i in inp:
    if i==nano:
        break;
    else:
        pos+=1

print("Menor valor: %d"%nano,end="\n")
print("Posicao: %d"%pos,end="\n")
