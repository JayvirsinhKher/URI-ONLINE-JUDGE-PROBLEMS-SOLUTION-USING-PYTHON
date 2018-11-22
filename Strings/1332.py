def letter_reco(s):
    t=0
    if len(s) ==3:
        if (s[0] in 'o'):
            if (s[1] in 'n'):
                print('1',end='\n')
            elif (s[2] in 'e'):
                print('1',end='\n')
        elif (s[1] in 'n') and (s[2] in 'e'):
            print('1',end='\n')


        if (s[0] in 't'):
            if (s[1] in 'w'):
                print('2',end='\n')
            elif (s[2] in 'o'):
                print('2',end='\n')
        elif (s[1] in 'w') and (s[2] in 'o'):
            print('2',end='\n')
    else:
        for i in range(len(s)):
            if s[i] in 'three':
                t+=1
        if t>=4:
            print('3',end='\n')
        
n = int(input())
for i in range(n):
    s = input()
    letter_reco(s)
        
