x = int(input())
n = 0
sum1 = 0
while True:
    z = int(input())
    if z>x:
        break
    else:
        pass
for i in range(x,z):
    if sum1>z:
        print(n,end="\n")
        break
    else:
        sum1 += i
        n += 1

