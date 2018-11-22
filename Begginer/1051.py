
sal = float(input())

if(sal>=0.00 and sal<=2000.00):
    tax = 0
    print("Isento",end="\n")
elif(sal>2000.00 and sal<=3000.00):
    tax = 0.08
    tax_free = sal - 2000.00
    tax_pay = tax_free*tax
    print("R$ %0.2f"%tax_pay,end="\n")
elif(sal>3000.00 and sal<=4500.00):
    tax = 0.18
    tax_free = sal - 2000.00
    if(tax_free >= 1000.00):
        tax_free_1 = tax_free - 1000
        tax_1 = 1000 * 0.08
        tax_2 = tax_free_1 * tax
    tax_pay = tax_1+tax_2
    print("R$ %0.2f"%tax_pay,end="\n")
else:
    tax = 0.28
    tax_free = sal - 2000.00
    if (tax_free >= 2500.00):
        tax_free_1 = tax_free - 2500.00
        tax_1 = tax_free_1 * tax
        tax_2 = 1000 * 0.08
        tax_3 = 1500 * 0.18
    tax_pay = tax_1+tax_2+tax_3
        
    print("R$ %0.2f"%tax_pay,end="\n")

            


    
