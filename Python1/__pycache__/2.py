number = int(input())
def factorial(num):
    if num > 0:
        fact = num*factorial(num - 1)
        return fact
    else:
        return 1    
Answer = factorial(number)

print(Answer)
