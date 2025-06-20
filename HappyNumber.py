# Happy numbers are numbers that eventually becomes 1 when replaced by the sum of the squares of its digits repeatedly
# List of numbers
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# If n == 1, the number is happy and returns true
# If n != 1, the number is unhappy and returns false
def Hpy_Number(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1

# Validate and returns true where number is happy
happy_nums = [n for n in numbers if Hpy_Number(n)]

print("Happy Numbers: ", happy_nums)
print("Total Happy Numbers in the list: ", len(happy_nums))
