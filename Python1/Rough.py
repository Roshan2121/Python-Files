from itertools import combinations as c
number_of_char = int(input())
list_of_chars = input().split(' ')
list_of_combinations = list(c(list_of_chars, 2))
print(list_of_combinations)
x = len(list_of_combinations)
print(x)
count = 0
for tuples in list_of_combinations:
    if 'a' in tuples:
        count += 1
print(count/x)
