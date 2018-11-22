
sth,stm,eth,etm= input().split(" ")
sth,stm,eth,etm = int(sth),int(stm),int(eth),int(etm)

dur = eth - sth
if(dur < 0):
    dur = 24 + (eth-sth)

mint = etm-stm
if(mint < 0):
    mint = 60 + (etm-stm)
    dur -=1

if(sth==eth and stm==etm):
    dur = 24
    mint = 0
 
print("O JOGO DUROU",dur,"HORA(S) E",mint,"MINUTO(S)",end="\n")
