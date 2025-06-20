# Given the list of numbers in which 3 numbers added to form target value
# Target value is 59
Num_list = [10, 20, 30, 9]
target = 59

def find_triplet(arr, target):
    n = len(arr)
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    return arr[i], arr[j], arr[k]
    return "No triplet found"

# Example usage
result = find_triplet(Num_list, target)
print("Triplet with sum", target, "is:", result)
