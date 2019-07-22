x = int(input())
value = (x>250)*((x-250)*10+500)+(True and (x<=250 and x>150))*(x-150)*5+(x>150)*100*2+(True and (x<=150 and x>50))*(x-50)*2+(x>50)*50+(x<=50)*x
print(value)
