
def fact(a):
    if a==0:
        return 1
    else:
        return a*fact(a-1)

    
while True:
    try:
        inpt = input()
        fsum = 0
        in1,in2 = inpt.split(" ")
        in1,in2 = int(in1),int(in2)
        fsum = fact(in1) + fact(in2)
        print(fsum,end="\n")
    except EOFError:
        break
        

