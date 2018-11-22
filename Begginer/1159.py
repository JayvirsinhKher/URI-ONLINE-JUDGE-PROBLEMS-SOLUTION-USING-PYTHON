
def esum(j):
    sum1 = 0
    for i in range(5):
        sum1 +=j
        j +=2
    print(sum1,end="\n")
    
while True:
    n = int(input())
    if n==0:
        break
    elif n%2==0:
        esum(n)
    else:
        esum(n+1)
