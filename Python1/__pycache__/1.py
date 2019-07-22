#divisible by 7 not divisible of 5

for i in range(2000, 2008):
    if i%7 == 0:
        start = i
        break
    else:
        continue
for i in range(start, 3201, 7):
    if i%7 == 0 and i%5 != 0:
        print(i)
