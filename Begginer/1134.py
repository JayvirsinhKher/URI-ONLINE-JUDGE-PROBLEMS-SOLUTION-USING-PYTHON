
print("MUITO OBRIGADO",end="\n")
alcohol = 0
gasoline = 0
diesel = 0
while True:
    x = int(input())
    if(x==1):
        alcohol +=1
    elif(x==2):
        gasoline +=1
    elif(x==3):
        diesel +=1
    elif(x==4):
        break
    else:
        pass

print("Alcool: %d"%alcohol,end="\n")
print("Gasolina: %d"%gasoline,end="\n")
print("Diesel: %d"%diesel,end="\n")
        
            

        
