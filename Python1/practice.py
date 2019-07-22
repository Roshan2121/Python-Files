import time
num = int(input())
x = time.time()
i = 1
while True:
    char = str(i)
    product = 1
    for chars in char:
        product = product*int(chars)
    if product%1000000007 == num:
        print(i)
        break
    else:
        i += 1
print(time.time() - x)    
