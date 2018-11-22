
in1 = int(input())
in2 = int(input())

sum1 = 0
if(in2 < 0):
    
    for i in range(in1,in2,-1):
        if i%2==1:
            sum1 +=i
else:
    for i in range(in2,in1):
        if i%2==1:
            sum1 +=i    

print(sum1,end="\n")
