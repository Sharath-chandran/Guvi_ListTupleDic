def first_non_repeating(lst):
    for num in lst:
        if lst.count(num) == 1:
            return num
    return None

# Example
numbers = [4, 5, 1, 2, 0, 5, 1, 4]
result = first_non_repeating(numbers)
print("First non-repeating element:", result)
