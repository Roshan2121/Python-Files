number = input()
list1 = number.split(',')
list2 = []
for i in range(int(list1[0])):
    list3 = []
    for j in range(int(list1[1])):
        num = i*j
        list3.append(num)
    list2.append(list3)

print(list2)    
