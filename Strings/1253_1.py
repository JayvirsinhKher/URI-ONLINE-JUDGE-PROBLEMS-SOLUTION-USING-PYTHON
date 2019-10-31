#ceaser cipher
test_cases = int(input())
op = ''
for i in range(test_cases):
    pt = input()
    key = int(input())
    s_len = len(pt)
    for j in range(s_len):
        op = op+chr(ord(pt[j])-key)
    print(op)
    op=''
