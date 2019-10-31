#URI 1873

test_cases = int(input())
for i in range(test_cases):
    r,s = input().split(' ')
    if r==s:
        print("empate")
    elif r == 'pedra':
        if s=='tesoura' or s=='lagarto':
            print('rajesh')
        else:
            print('sheldon')
    elif r == 'papel':
        if s=='pedra' or s=='spock':
            print('rajesh')
        else:
            print('sheldon')
    elif r == 'tesoura':
        if s=='papel' or s=='lagarto':
            print('rajesh')
        else:
            print('sheldon')
    elif r == 'lagarto':
        if s=='papel' or s=='spock':
            print('rajesh')
        else:
            print('sheldon')
    elif r == 'spock':
        if s=='pedra' or s=='tesoura':
            print('rajesh')
        else:
            print('sheldon')
