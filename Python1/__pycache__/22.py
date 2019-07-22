list1 = input().split(" ")
list1.sort()
count = 1
for i in range(1, len(list1)):
    if list1[i] == list1[i - 1]:
        count += 1
    else:
        print(list1[i - 1], ':', count)
        count = 1
    
