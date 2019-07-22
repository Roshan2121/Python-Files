a = int(input())
b = int(input())
c = int(input())
if a>=c:
    if a>=b:
        print("THe biggest number is",a)
    else:
        print("The biggest number is",b)
elif b>=c:
    print("The biggest number is",b)
else:
    print("The biggest number is",c)
