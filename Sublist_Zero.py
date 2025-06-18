def has_zero_sum_sublist(arr):
    seen_sums = set()
    total = 0
    for num in arr:
        total += num
        if total == 0 or total in seen_sums:
            return True
        seen_sums.add(total)
    return False

# Example usage
lst = [4, 2, -3, 1, 6]
if has_zero_sum_sublist(lst):
    print("There is a sub-list with sum equal to 0")
else:
    print("No sub-list with sum equal to 0")
