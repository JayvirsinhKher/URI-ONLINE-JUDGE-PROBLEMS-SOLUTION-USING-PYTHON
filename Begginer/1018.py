
Rs = int(input())
print(Rs,end="\n")
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

print(hundredNotes,"nota(s) de R$ 100,00",end="\n")
print(fiftyNotes,"nota(s) de R$ 50,00",end="\n")
print(twentyNotes,"nota(s) de R$ 20,00",end="\n")
print(tenNotes,"nota(s) de R$ 10,00",end="\n")
print(fiveNotes,"nota(s) de R$ 5,00",end="\n")
print(twoNotes,"nota(s) de R$ 2,00",end="\n")
print(oneNotes,"nota(s) de R$ 1,00",end="\n")
