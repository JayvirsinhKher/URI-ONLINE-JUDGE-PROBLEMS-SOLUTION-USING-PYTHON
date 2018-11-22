
n=100

a =[int(input()) for i in range(n)]

large = max(a)

for i in range(n):
    if a[i] == large:
        print(large,end="\n")
        print(i+1,end="\n")
        break


        
    
        


