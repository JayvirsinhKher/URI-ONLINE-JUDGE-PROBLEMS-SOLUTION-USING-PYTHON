
sal = float(input())

if (sal>=0 and sal<=400):
    readjust_p = 15
if (sal>400 and sal<=800):
    readjust_p = 12
if (sal>800 and sal<=1200):
    readjust_p = 10
if (sal>1200 and sal<=2000):
    readjust_p = 7
if (sal>2000):
    readjust_p = 4

readjust_m = (sal*readjust_p)/100
new_sal = sal + readjust_m

print("Novo salario: %0.2f"%new_sal,end="\n")
print("Reajuste ganho: %0.2f"%readjust_m,end="\n")
print("Em percentual: %d"%readjust_p,"%",end="\n")


    
