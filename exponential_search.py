import timeit
def binary_search(arr, target, left, right):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def exponential_search(arr, target):
    if arr[0] == target:
        return 0
    i = 1
    n = len(arr)
    while i < n and arr[i] <= target:
        i *= 2
    return binary_search(arr, target, i // 2, min(i, n) - 1)


def exponential_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)



# def binary_search_recursive(arr, target, left, right):
#     if left > right:
#         return -1

#     mid = left + (right - left) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return binary_search_recursive(arr, target, mid + 1, right)
#     else:
#         return binary_search_recursive(arr, target, left, mid - 1)

# def exponential_search_recursive(arr, target, i=1):
#     n = len(arr)
#     if arr[0] == target:
#         return 0
#     if i < n and arr[i] < target:
#         return exponential_search_recursive(arr, target, i * 2)
#     return binary_search_recursive(arr, target, i // 2, min(i, n) - 1)

# Example array and target value
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41]
target = 29

# Test iterative Exponential Search
result_iterative = exponential_search(arr, target)
print(f"Iterative Exponential Search: Target {target} found at index {result_iterative}")

