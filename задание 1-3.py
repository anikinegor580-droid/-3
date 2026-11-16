def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print(linear_search([5, 3, 7, 1, 4], 1))
print(linear_search([5, 3, 7, 1, 4], 6))
print(linear_search([1, 2, 2, 3], 2))
print(linear_search([], 1))


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
            
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7], 4))
print(binary_search([1, 2, 3, 4, 5, 6, 7], 8))
print(binary_search([], 1))
