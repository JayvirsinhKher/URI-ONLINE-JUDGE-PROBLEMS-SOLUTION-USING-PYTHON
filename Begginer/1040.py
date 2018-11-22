

n1,n2,n3,n4=input().split(" ")

n1=float(n1)
n2=float(n2)
n3=float(n3)
n4=float(n4)

#weight 2,3,4,1 total=10

avg =((2*n1)+(3*n2)+(4*n3)+(1*n4))/(2+3+4+1)

print("Media: %0.1f"%avg,end="\n")


if (avg >= 7.0):
    print("Aluno aprovado.",end="\n")
elif (avg < 5.0):
    print("Aluno reprovado.",end="\n")
elif (avg >= 5.0 and avg <= 6.9):
    print("Aluno em exame.")
    n5 = float(input())
    print("Nota do exame:",n5,end="\n")
    new_avg = (avg+n5)/2.0
    if (new_avg >=5.0):
        print("Aluno aprovado.",end="\n")
    else:
        print("Aluno reprovado.",end="\n")
    print("Media final: %0.1f"%new_avg,end="\n")
