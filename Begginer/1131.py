def ck():
    global inter
    global gremio
    global empates
    global i
    while True:
        print("Novo grenal (1-sim 2-nao)",end="\n")
        a,b = map(int,input().split())
        if a>b:
            inter +=1
        elif a<b:
            gremio +=1
        else:
            empates +=1
            
        i+=1
        
        x = int(input())
        if(x == 1):
            pass
        else:
            break
        
i = 0
inter = 0
gremio = 0
empates = 0
ck()
print(i,"grenais",end="\n")
print("Inter:%d"%inter,end="\n")
print("Gremio:%d"%gremio,end="\n")
print("Empates:%d"%empates,end="\n")

if(inter>gremio):
    print("Inter venceu mais",end="\n")
elif(inter<gremio):
    print("Gremio venceu mais",end="\n")
else:
    print("Não houve vencedor",end="\n")

        
