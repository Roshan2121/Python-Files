answer = 0
control = True
print("Enter stop to end the calculations")
while control:
    data = input()
    list1 = []
    if data == 'stop':
        control = False
    else:    
        if answer == 0:
            answer = eval(data)
        else:
            answer_to_string = str(answer)
            list1.append(answer_to_string)
            list1.append(data)
            delimiter = ""
            Final_string_to_be_valued = delimiter.join(list1)
            answer = eval(Final_string_to_be_valued)
        print(answer)    
        
    
    
