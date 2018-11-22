
n = int(input())

while n>0:
    in1,in2 = input().split(" ")
    in1,in2=int(in1),int(in2)
    if(in2 == 0):
        print('divisao impossivel',end="\n")
    else:
        print('%0.1f'%(in1/in2),end="\n")
    n -=1
