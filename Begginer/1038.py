

code,amount = input().split(" ")
code=int(code)
amount=int(amount)

tbl = { 1:4.00,
        2:4.50,
        3:5.00,
        4:2.00,
        5:1.50
       }
paid = amount * tbl[code]

print("Total: R$ %0.2f"%paid,end="\n")
