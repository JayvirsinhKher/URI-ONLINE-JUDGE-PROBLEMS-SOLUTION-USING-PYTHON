

p1,noUnit1,noUnitPrice1 = input().split(" ")
p2,noUnit2,noUnitPrice2 = input().split(" ")

noUnit1 = int(noUnit1)
noUnit2 = int(noUnit2)

noUnitPrice1 = float(noUnitPrice1)
noUnitPrice2 = float(noUnitPrice2)

total = (noUnit1*noUnitPrice1)+(noUnit2*noUnitPrice2)

print("VALOR A PAGAR: R$ %0.2f"%total)
