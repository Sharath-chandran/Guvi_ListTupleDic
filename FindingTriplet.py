def find_triplet(arr, target):
    n = len(arr)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    return (arr[i], arr[j], arr[k])
    return "No triplet found"

# Example usage
lst = [10, 20, 30, 9]
target = 59
result = find_triplet(lst, target)
print("Triplet with sum", target, "is:", result)
