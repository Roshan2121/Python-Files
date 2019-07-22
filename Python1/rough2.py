def print_formatted(number):
    for i in range(1, number + 1):
        print(' '*(len(bin(number)) - len(bin(1)) - 1), ' '*(len(str(number)) - len(str(i))) + str(i),' '*(len(bin(number)) - len(bin(1)) - 1), ' '*(len(oct(number)) - len(oct(i))) + (oct(i))[2:],' '*(len(bin(number)) - len(bin(1)) - 1), ' '*(len(hex(number)) - len(hex(i))) + (hex(i).upper())[2:], ' '*(len(bin(number)) - len(bin(i))) + (bin(i))[2:])

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    
