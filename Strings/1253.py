#ceaser cipher
test_cases = int(input())
op = ''
fop = list()
for i in range(test_cases):
    pt = input()
    key = int(input())
    s_len = len(pt)
    for j in range(s_len):
        a = ord(pt[j])-key
        if a<ord('A'):
            b = ord('A') - a
            op = op + chr(91-b)
        else:
            op = op+chr(a)
    fop.append(op)
    op=''
for i in fop:
    print(i)
