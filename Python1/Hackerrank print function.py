Number = int(input())
list1 = []
for i in range(1,Number+1):
    data = str(i)
    list1.append(data)

delimiter = ""
string = delimiter.join(list1)
print(string)
