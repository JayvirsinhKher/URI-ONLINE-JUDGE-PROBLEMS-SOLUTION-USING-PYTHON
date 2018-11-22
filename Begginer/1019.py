
time = int(input()) #in seconds

remSec = time%60 #it gives seconds

mint = int(time/60) 

remMin = mint%60  #it gives min

hours = int(mint/60)

remHours = hours%60 #it gives hours

print(str(remHours)+str(":")+str(remMin)+str(":")+str(remSec),end="\n")
