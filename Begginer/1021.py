
total = float("%0.2f"%float(input()))
Rs = int(total)
rem = (total - Rs)*100

hundredNotes = int(Rs/100)
Rs = Rs%100
fiftyNotes = int(Rs/50)
Rs = Rs%50
twentyNotes = int(Rs/20)
Rs = Rs%20
tenNotes = int(Rs/10)
Rs = Rs%10
fiveNotes = int(Rs/5)
Rs = Rs%5
twoNotes = int(Rs/2)
Rs = Rs%2
oneNotes = int(Rs/1)

fiftyCoin = int(rem/50)
rem = rem%50

twentyfiveCoin = int(rem/25)
rem = rem%25

tenCoin = int(rem/10)
rem = rem%10

fiveCoin = int(rem/5)
rem = rem%5

oneCoin = int(rem/1)

print("NOTAS:",end="\n")
print(hundredNotes,"nota(s) de R$ 100.00",end="\n")
print(fiftyNotes,"nota(s) de R$ 50.00",end="\n")
print(twentyNotes,"nota(s) de R$ 20.00",end="\n")
print(tenNotes,"nota(s) de R$ 10.00",end="\n")
print(fiveNotes,"nota(s) de R$ 5.00",end="\n")
print(twoNotes,"nota(s) de R$ 2.00",end="\n")
print("MOEDAS:",end="\n")
print(oneNotes,"moeda(s) de R$ 1.00",end="\n")
print(fiftyCoin,"moeda(s) de R$ 0.50",end="\n")
print(twentyfiveCoin,"moeda(s) de R$ 0.25",end="\n")
print(tenCoin,"moeda(s) de R$ 0.10",end="\n")
print(fiveCoin,"moeda(s) de R$ 0.05",end="\n")
print(oneCoin,"moeda(s) de R$ 0.01",end="\n")
