# Under the given 3 lists, Find the duplicates in the 3 lists
list_1 = [17, 34, 45, 99, 101]
list_2 = [45, 99, 101, 127, 143]
list_3 = [101, 127, 143, 165, 179]

# Finding duplicates across all three lists
# Comparing all the 3 lists
duplicates = set(list_1) & set(list_2) & set(list_3)
print("Duplicate number in all three lists:", duplicates)
