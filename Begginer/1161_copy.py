day1 = input().split(
d1 = int(day1[1])

hms1 = input().split(" : ")
h1,m1,s1 = list(map(int,hms1))


day2 = input().split()
d2 = int(day2[1])

hms2 = input().split(" : ")
h2,m2,s2 = list(map(int,hms2))

d = d2 - d1

h = h2 - h1
if(h < 0):
    h = 24 + h
    d = d - 1

m = m2 - m1 
if(m < 0):
    m = 60 + m
    h = h - 1

s = s2 - s1
if(s < 0):
    s = 60 + s
    m = m - 1

if(d <= 0):
    d = 0

print("%d dia(s)" %d,end="\n")
print("%d hora(s)" %h,end="\n")
print("%d minuto(s)" %m,end="\n")
print("%d segundo(s)" %s,end="\n")
