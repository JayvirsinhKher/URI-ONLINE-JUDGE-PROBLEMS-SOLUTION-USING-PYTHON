

sellerName = input()

monthFixedSalary = float(input())

monthSalesTotal = float(input())

TOTAL = monthFixedSalary + (0.15 * monthSalesTotal)

print("TOTAL = R$ %0.2f"%TOTAL,end="\n")
