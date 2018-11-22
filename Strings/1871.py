def cal(m,n):
    add = m+n
    add_s = str(add)
    new_s =''
    for i in add_s:
        if i is not '0':
            new_s +=i
    
    print(int(new_s),end="\n")
    
while True:
    m,n = map(int,input().split())
    if m==0 and n==0:
        break
    else:
        cal(m,n)
