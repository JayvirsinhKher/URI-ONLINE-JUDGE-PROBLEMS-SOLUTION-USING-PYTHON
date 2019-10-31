test_cases = int(input())
op = ''
for i in range(test_cases):
    a,b=input().split(' ')
    i=0
    while i<max(len(a),len(b)):
        if i<len(a):
            op = op + a[i]
        if i<len(b):
            op = op + b[i]
        i = i+1
    print(op)
    op = ''
        
