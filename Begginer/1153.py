
n = int(input())
fact = 1
if n>0 and n<13:
    for i in range(1,n+1):
        fact *=i
print(fact,end="\n")
