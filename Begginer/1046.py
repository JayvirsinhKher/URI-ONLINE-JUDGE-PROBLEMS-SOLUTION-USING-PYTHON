
st,et= input().split(" ")
st,et = int(st),int(et)

if (st >= et):
    a = 24 - st
    b = et - 0
    dur = a + b
else:
    a = 24 - st
    b = et - 24
    dur = a + b

print("O JOGO DUROU",dur,"HORA(S)")
