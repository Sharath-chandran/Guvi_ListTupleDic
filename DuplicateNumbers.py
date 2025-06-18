# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

# Find duplicates across all three lists
duplicates = set(list1) & set(list2) & set(list3)
print("Duplicates in all three lists:", list(duplicates))
