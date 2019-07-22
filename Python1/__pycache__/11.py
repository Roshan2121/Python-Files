list1 = input().split(',')
list2 = []
for number in list1:
    if (number[-1] == '0' or number[-1] == '0') and number[0] != '0':
        list2.append(number)    
print(','.join(list2))        
