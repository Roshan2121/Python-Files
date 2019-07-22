list1 = input().split(' ')
list1.sort()
list2 = []
for i in range(0, len(list1) - 2):
    if list1[i] == list1[i + 1]:
        del list1[i + 1]
print(' '.join(list1))
