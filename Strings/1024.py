#simple Encryption Problem
n =int(input())
for x in range(n):
    a = input()
    b = ""
    for i in range(len(a)):
        if (a[i]>='A' and a[i]<='Z') or (a[i]>='a' and a[i]<='z'):
            b += chr(ord(a[i])+3)
        else:
            b += a[i]

    b = b[-1::-1]
    e = b[:int(len(b)/2)]
    for j in range(int(len(b)/2),len(b)):
            e += chr(ord(b[j])-1)

    print(e)
