def find_min_in_rotated(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high) // 2
        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid
    return arr[low]

# Example
rotated_list = [5, 6, 7, 1, 2, 3, 4]
print("Minimum element is:", find_min_in_rotated(rotated_list))
