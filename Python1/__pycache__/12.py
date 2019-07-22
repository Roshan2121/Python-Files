list1 = []
for i in range(1000, 3001):
    length = len(str(i))
    for j in range(length - 1, -1, -1):
        if (i//pow(10, j))%2 != 0:
            break
    if j == 0:
        list1.append(str(i))
    else:
        i = i + pow(10, j)
        list2 = []
        for letter in str(i):
            list2 = letter
        print(list2)    
        for k in range(j - 1, -1, -1):
            del list2[k]
            list2.append('0')
        i = int(''.join(list2)) - 2
print(','.join(list1))        
        
