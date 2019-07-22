test_cases = int(input())
def finder(number):
    global count
    global controller
    controller += 1
    sum1 = 0
    to_be_added = 1
    if(number > 0):
        for j in range(controller):
            count += 1
            to_be_added = count*to_be_added
        print(to_be_added)    
        sum1 = to_be_added + finder(number-1)   
    return sum1
    
for i in range(test_cases):
    count = 0
    number = int(input())
    controller = 0
    answer = finder(number)
    print(answer)
