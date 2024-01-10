
import timeit
def binary_search(array, target):
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (low + high) // 2

        if array[mid] == target:
            return mid
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def binary_search_wrapper1(array, target):
    return binary_search(arr, target)

def binary_search_wrapper(func, *args, **kwargs):
    return func(*args, **kwargs)

# def binary_search_recursive(arr, target, low, high):
#     if low <= high:
#         mid = (low + high) // 2

#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             return binary_search_recursive(arr, target, mid + 1, high)
#         else:
#             return binary_search_recursive(arr, target, low, mid - 1)

#     return -1

#def binary_search
numbers = range(1, 1001)
test_data = ", ".join(map(str, numbers))
target = 11
arr = list(map(int, test_data.split(",")))
execution_time = timeit.timeit("binary_search_wrapper(binary_search, arr, target)", globals=globals(), number=1)   
result = binary_search_wrapper(binary_search, arr, target)
print(f"Time taken to execute: {execution_time:.6f} seconds")
print(f"Resoult found in index: {result} ")