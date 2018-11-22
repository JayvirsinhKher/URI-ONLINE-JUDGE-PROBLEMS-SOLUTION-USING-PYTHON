
A,B,C = input().split(" ")

A = float(A)
B = float(B)
C = float(C)


A_Triangle = (C*A/2)
print("TRIANGULO: %0.3f"%A_Triangle,end="\n")
A_Circle = (3.14159*C*C)
print("CIRCULO: %0.3f"%A_Circle,end="\n")
A_Trapazium = ((A+B)/2)*C
print("TRAPEZIO: %0.3f"%A_Trapazium,end="\n")
A_Square = B*B
print("QUADRADO: %0.3f"%A_Square,end="\n")
A_Rect = A*B
print("RETANGULO: %0.3f"%A_Rect,end="\n")
