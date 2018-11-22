
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

pos = 0
neg = 0
even = 0
odd = 0

def check(a):
    global pos
    global neg
    global even
    global odd
    if(a!=0):
        if(a>0):
            pos+=1
            if(a%2==0):
                even+=1
            else:
                odd+=1
        else:
            neg+=1
            if(a%2==0):
                even+=1
            else:
                odd+=1
    else:
        even+=1
        
check(a)
check(b)
check(c)
check(d)
check(e)

print(even,"valor(es) par(es)",end="\n")
print(odd,"valor(es) impar(es)",end="\n")
print(pos,"valor(es) positivo(s)",end="\n")
print(neg,"valor(es) negativo(s)",end="\n")
