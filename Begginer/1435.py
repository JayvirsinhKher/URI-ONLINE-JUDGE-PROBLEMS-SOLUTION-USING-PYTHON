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

    val = 1
    top = 0
    left = 0
    low = n - 1
    right = n - 1

    if (n % 2 == 0):
        mid = n / 2

    else:
        mid = (n + 1) / 2


    while (val <= mid):
        i = left
        while (i <= right):
            ans[top][i] = val
            ans[low][i] = val
            i+=1

        i = (top + 1)
        while ( i < low):
            ans[i][left] = val
            ans[i][right] = val
            i+=1

        val+=1
        top+=1
        low-=1
        left+=1
        right-=1

    for i in range(n):
        tx = ''
        for j in range(n):
            tx += " %3d" %ans[i][j]
        print(tx[1:])
    print("")
