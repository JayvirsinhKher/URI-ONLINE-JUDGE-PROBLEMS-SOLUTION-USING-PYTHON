
totalSpent = int(input()) # hours
avgSpeed = int(input()) #km/h

totalKms = totalSpent*avgSpeed

fuelNeeded = float(totalKms/12)  #12km/l given

print("%0.3f"%fuelNeeded,end="\n")
