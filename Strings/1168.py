def led(s):
    l = 0
    for j in range(len(s)):
        dic={'1':2,
             '2':5,
             '3':5,
             '4':4,
             '5':5,
             '6':6,
             '7':3,
             '8':7,
             '9':6,
             '0':6}
        l += dic[s[j]]
    print(l,'leds',end="\n")
        


n = int(input())
if n>=1 and n<=2000:
    for i in range(n):
        s = input()
        led(s)
        
