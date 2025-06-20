# Finding the non-repeating numbers from the list
numbers = [4, 5, 1, 2, 0, 5, 1, 4]

# Defines a function to identify the first non-repeating number from the list
def first_non_repeating(lst):
    for num in lst:
        if lst.count(num) == 1:
            return num
    return None

result = first_non_repeating(numbers)
print("First non-repeating number:", result)
