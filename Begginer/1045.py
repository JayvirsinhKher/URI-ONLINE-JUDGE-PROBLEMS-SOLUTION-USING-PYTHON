
A,B,C = input().split(" ")
A,B,C = float(A),float(B),float(C)

m1 = max(A,max(B,C))
m2 = None
m3 = None

if (m1 == A):
    m2 =max(B, C)
    m3 =min(B, C)
if (m1 == A):
    m2 =max(B, C)
    m3 =min(B, C)
if (m1 == B):
    m2 =max(A, C)
    m3 =min(A, C)
if (m1 == C):
    m2 =max(B, A)
    m3 =min(B, A)
  
if (m1 >= (m2 + m3)):
    print("NAO FORMA TRIANGULO",end="\n")
elif (m1**2 > ((m2**2)+(m3**2))):
    print("TRIANGULO OBTUSANGULO",end="\n")
if (m1**2 == ((m2**2)+(m3**2))):
    print("TRIANGULO RETANGULO",end="\n")

if (m1**2 < ((m2**2)+(m3**2))):
    print("TRIANGULO ACUTANGULO",end="\n")
if ((m1 == m2) and (m1 == m3)):
    print("TRIANGULO EQUILATERO",end="\n")
if (((m1 == m2) and (m1 != m3)) or ((m1 == m3) and (m1 != m2)) or ((m2 == m3) and (m2 != m1)) ):
      print("TRIANGULO ISOSCELES",end="\n")

