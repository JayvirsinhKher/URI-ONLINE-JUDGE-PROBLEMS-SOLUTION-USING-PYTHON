#Array Hash

test_cases = int(input())
tmp_summ = 0
for i in range(test_cases):
    no_of_input_line = int(input())
    ip_l = list()
    tmp_index = 0
    summ = 0
    for i in range(no_of_input_line):
        ip_l.append(input())
    #print("length of ip_l : ",len(ip_l))
    for j in ip_l:
        element_input = tmp_index
        element_position = 0
        in_index = 0
        #print("length of j : ",len(j))
        #print("length of ip_l[tmp_index] : ",len(ip_l[tmp_index]))
        #print("tmp_inex",tmp_index)
        while in_index < len(j):
            ap = ord(ip_l[tmp_index][in_index]) - 65
            tmp_summ = tmp_summ + ap + element_input + element_position
            element_position +=1
            in_index +=1
        tmp_index += 1
        summ +=tmp_summ
        tmp_summ = 0
    print(summ)
                      
            
            
            
            
            
            
        
            
    
        
