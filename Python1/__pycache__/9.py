list1 = []
while True:
	s = input()
	if s:
		list1.append(s)
	else:
		break
for string in list1:
    str_length = len(string)
    string_capital = ''
    for i in range(0, str_length):
        if ord(string[i]) >= 97 and ord(string[i]) <= 122:
            string_capital = string_capital + chr(ord(string[i]) - 32)
        else:
            string_capital = string_capital + string[i]
    print(string_capital)  
