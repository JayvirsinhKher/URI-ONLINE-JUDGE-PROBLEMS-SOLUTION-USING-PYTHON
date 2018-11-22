
a,b,c = input().split(" ")
a=int(a)
b=int(b)
c=int(c)

MaiorAB = int((a+b+abs(a-b))/2)
MaiorABC = int((MaiorAB+c+abs(MaiorAB-c))/2)

print(str(MaiorABC)+" eh o maior",end="\n")
