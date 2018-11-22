a = None
b = None

while True:
    a = float(input())
    if (a>=0 and a<=10):
        break
    else:
        print("nota invalida",end="\n")
while True:
    b = float(input())
    if (b>=0 and b<=10):
        break
    else:
        print("nota invalida",end="\n")

med = (a+b) / 2.0

print("media = %0.2f"%med,end="\n")

while True:
    x = int(input())
    print("novo calculo (1-sim 2-nao)",end="\n")
    if(x == 1):
        while True:
            a = float(input())
            if (a>=0 and a<=10):
                break
            else:
                pass
        while True:
            b = float(input())
            if (b>=0 and b<=10):
                break
            else:
                pass

        med = (a+b) / 2.0

        print("media = %0.2f"%med,end="\n")
    elif(x == 2):
        break
    else:
        pass

        
        
