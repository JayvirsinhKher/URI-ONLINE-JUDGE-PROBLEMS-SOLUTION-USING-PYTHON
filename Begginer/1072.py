
n = int(input())

a = [int(input()) for i in range(1,n+1)]

in1 = 0
out1 = 0

for m in a:
    if m in range(10,20):
        in1 += 1
    else:
        out1 += 1

print(in1,"in",end="\n")
print(out1,"out",end="\n")


