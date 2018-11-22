
A,B,C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)

d = (B**2)-(4*A*C)

if(A!=0 and d>0):
    R1 = (-B+(d**0.5))/(2*A)
    print("R1 = %0.5f"%R1,end="\n")
    R2 = (-B-(d**0.5))/(2*A)
    print("R2 = %0.5f"%R2,end="\n")
else:
    print("Impossivel calcular",end="\n")

