
n1,n2,n3 = input().split(" ")
n1,n2,n3=int(n1),int(n2),int(n3)
a,b,c = n1,n2,n3

if (n1<n2 and n1<n3):
    print(n1,end="\n")
    if(n2<n3):
        print(n2,end="\n")
        print(n3,end="\n")
    else:
        print(n3,end="\n")
        print(n2,end="\n")
elif (n2<n1 and n2<n3):
    print(n2,end="\n")
    if(n1<n3):
        print(n1,end="\n")
        print(n3,end="\n") 
    else:
        print(n3,end="\n")
        print(n1,end="\n") 
elif (n3<n2 and n3<n1):
    print(n3,end="\n")
    if(n2<n1):
        print(n2,end="\n")
        print(n1,end="\n")
    else:
        print(n1,end="\n")
        print(n2,end="\n")

print(end="\n")
print(a,end="\n")
print(b,end="\n")
print(c,end="\n")
