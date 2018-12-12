while True:
    n = int(input())

    if n==0:
        break
    ans =  list()

    for i in range(n):
        tmp = list()
        for j in range(n):
            tmp.append(1)
        ans.append(tmp)
        
    top = 0
    left = 0
    m = n
    
    while (m >= 1):
        i = left
        val = 1
        while (i <= n-1):
            ans[left][i] = val
            ans[i][top] = val
            i+=1
            val+=1
        left+=1
        top+=1
        m-=1

    for i in range(n):
        tx = ''
        for j in range(n):
            tx += " %3d" %ans[i][j]
        print(tx[1:])
    print("")
