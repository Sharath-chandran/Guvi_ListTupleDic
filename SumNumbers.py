def sum_first_last(n):
    num_str = str(abs(n))
    return int(num_str[0]) + int(num_str[-1])

number = 12345
print("Sum of first and last digit:", sum_first_last(number))
