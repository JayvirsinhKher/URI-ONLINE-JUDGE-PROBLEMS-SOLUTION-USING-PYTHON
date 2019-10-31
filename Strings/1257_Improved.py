#Array Hash

# Improve Version less time consuming

test_cases = int(input())
for i in range(test_cases):
    no_of_input_line = int(input())
    summ = 0
    line = 0
    for i in range(no_of_input_line):
        a = input()
        pos = 0
        tmp_summ = 0
        while pos<len(a):
            ap = ord(a[pos]) - 65
            tmp_summ = tmp_summ + ap + line + pos
            pos+=1
        line +=1
        summ += tmp_summ
    print(summ)
                      
            
            
            
            
            
            
        
            
    
        
