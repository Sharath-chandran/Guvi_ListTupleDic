# Defining sum of first and last numbers of the integer itself
number = -234509

def sum_first_last(n):
# abs(n), this converts negative numbers to positive
# str, this converts the number into string so that easily access individual digits
    num_str = str(abs(n))
# Sum of first and last digit
    return int(num_str[0]) + int(num_str[-1])


print("Sum of first and last digit:", sum_first_last(number))
