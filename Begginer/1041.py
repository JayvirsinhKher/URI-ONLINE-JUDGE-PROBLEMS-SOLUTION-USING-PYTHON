
x,y = input().split(" ")
x = float(x)
y = float(y)

    
if (x==0.0 and y==0.0):
    print("Origem",end="\n")
elif (x==0.0):
    print("Eixo Y",end="\n")
elif (y==0.0):
    print("Eixo X",end="\n")
elif (x > 0.0 and y > 0.0):
    print("Q1",end="\n")
elif (x < 0.0 and y > 0.0):
    print("Q2",end="\n")
elif (x < 0.0 and y < 0.0):
    print("Q3",end="\n")
elif (x > 0.0 and y < 0.0):
    print("Q4",end="\n")
