
tc = int(input())

inp = [input() for i in range(tc)]

ans = list()

for i in range(tc):
    sum1 = 0
    in1,in2 = inp[i].split(" ")
    in1 = int(in1)
    in2 = int(in2)
    if(in1>=in2):
        for j in range(in2+1,in1):
            if(j%2==1):
                sum1 += j
    else:
        for j in range(in1+1,in2):
            if(j%2==1):
                sum1 += j
    ans.append(sum1)

for a in ans:
    print(a,end="\n") 
        
        


