
n = float(input())

if (n>=0 and n<=25):
    print("Intervalo [0,25]",end="\n")
elif (n>25 and n<=50):
    print("Intervalo (25,50]",end="\n")
elif (n>50 and n<=75):
    print("Intervalo (50,75]",end="\n")
elif (n>75 and n<=100):
    print("Intervalo (75,100]",end="\n")
else:
    print("Fora de intervalo",end="\n")

