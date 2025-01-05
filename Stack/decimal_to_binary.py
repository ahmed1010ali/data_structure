def divide_by_2(decimal_number):
    stack = []
    while decimal_number > 0:
        remainder = decimal_number % 2
        stack.append(remainder)
        decimal_number = decimal_number // 2
    binary_number = ""
    while stack:
        binary_number += str(stack.pop())
    return binary_number

print(divide_by_2(233))  
