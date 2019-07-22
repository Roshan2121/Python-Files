string = input()
list1 = string.split(',')
list1.sort()
delimiter = ','
string = delimiter.join(list1)
print(string)
