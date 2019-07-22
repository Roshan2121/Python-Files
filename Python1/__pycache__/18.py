password = input()
flag = 0
Dict = {'count_small_letters': 0, 'count_number': 0, 'count_capital_letters': 0, 'count_characters': 0}
for character in password:
    if character >= 'a' and character <= 'z':
        Dict['count_small_letters'] = Dict['count_small_letters'] + 1
    elif character >= '1' and character <= '9':
        Dict['count_number'] = Dict['count_number'] + 1
    elif character >= 'A' and character <= 'Z':
        Dict['count_capital_letters'] = Dict['count_capital_letters'] + 1
    elif character == '$' or character == '#' or character == '@':
        Dict['count_characters'] = Dict['count_characters'] + 1
for check in Dict:
    if Dict[check] == 0:
        flag = 1
        break
if flag == 0:
    print("Valid Password")
else:
    print("Invalid password")
