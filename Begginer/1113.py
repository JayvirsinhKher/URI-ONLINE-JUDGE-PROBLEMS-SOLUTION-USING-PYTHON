
ans = list()

while True:
    in1 = [input()]
    n1,n2 = in1[0].split(" ")
    n1,n2 = int(n1),int(n2)
    if(n1 > n2):
        ans.append('Decrescente')
    elif(n2>n1):
        ans.append('Crescente')
    else:
        break   

for i in ans:
    print(i,end="\n")
