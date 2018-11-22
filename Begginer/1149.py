"""
a=int(input())
n=0
while True:
    if n<=0:
        n = int(input())
    else:
        break

sum1 = 0
for i in range(a,a+n):
    sum1 +=i
print(sum1,end="\n")
"""
"""
a,n=map(int,input().split(" "))
while True:
    if n<=0:
        n = int(input())
    else:
        break
    
sum1 = 0
for i in range(a,a+n):
    sum1 +=i
print(sum1,end="\n")
"""

list1 = list(map(int,input().split(" ")))
a = 'j'
n = 0

for i in list1:
    if a=='j':
        a = i
    else:
        if i>0:
            n = i
            break

sum1 = 0
for i in range(a,a+n):
    sum1 +=i
print(sum1,end="\n")
