
A,B,C = input().split(" ")
A,B,C=float(A),float(B),float(C)

if((A+B > C) and (B+C > A) and (A+C > B)):
    #valid
    print("Perimetro = %0.1f"%(A+B+C),end="\n")
else:
    #invalid
    print("Area = %0.1f"%(((A+B)/2)*C),end="\n")
    

