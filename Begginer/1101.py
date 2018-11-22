
in1 = [input() for i in range(3)]

p1 = list()
p2 = list()

for i in range(3):
    m,n = in1[i].split(" ")
    p1.append(int(m))
    p2.append(int(n))
    
for i in range(3):
    sum1 = 0
    if(p1[i] > 0 and p2[i] > 0 ):
        if(p1[i] > p2[i]):
            while p2[i] <= p1[i]:
                print(p2[i],end=" ")
                sum1 += p2[i]
                p2[i] += 1
        else:
            while p1[i] <= p2[i]:
                print(p1[i],end=" ")
                sum1 += p1[i]
                p1[i] += 1
        print("Sum=%d"%sum1,end="\n")
    else:
        break
        


