def min_op(inp,out):
    min_o = 0
    for i in range(len(inp)):
        j = ord(inp[i])
        k = ord(out[i])
        while j!=k:
            if j==122:
                j = 97
                min_o+=1
            else:
                j+=1
                min_o+=1
            
    print(min_o,end="\n")
        
n = int(input())
if n<=100:
    for i in range(n):
        inp,out = input().split()
        min_op(inp,out)
        
