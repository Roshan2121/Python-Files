Number = int(input())
first = 0
runner = 0
for i in range(Number):
    data = int(input())
    if first == 0:
        first = data
    else:
        if data > first:
            runner = first
            first = data    
print(runner)
