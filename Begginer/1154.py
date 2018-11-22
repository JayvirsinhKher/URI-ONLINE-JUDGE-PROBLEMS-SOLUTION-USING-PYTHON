
l1 = list()
while True:
    n = int(input())
    if n>=0:
        l1.append(n)
    else:
        break
sum1 = sum(l1)
avg = sum1/len(l1)

print("%0.2f"%avg,end="\n")
