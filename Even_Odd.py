# Given list of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# n % 2 == 0 is true only when n is even
even_numbers = [n for n in numbers if n % 2 == 0]
odd_numbers = [n for n in numbers if n % 2 != 0]

print("Even Numbers: ", even_numbers)
print("Odd Numbers: ", odd_numbers)
