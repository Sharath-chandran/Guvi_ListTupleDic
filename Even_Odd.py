nums = [2, 3, 6, 11, 17, 23, 28, 32, 40, 48, 51, 57, 66, 72, 77, 80, 88, 99, 101, 108]

even_nums = [n for n in nums if n % 2 == 0]
odd_nums = [n for n in nums if n % 2 != 0]

print("Even Numbers:", even_nums)
print("Odd Numbers:", odd_nums)
