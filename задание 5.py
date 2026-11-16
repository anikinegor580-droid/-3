def quick_sort(arr):
    if len(arr) <= 1:
        return arr.copy()
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
if __name__ == "__main__":
    print(quick_sort([4, 2, 7, 1, 3, 5]))  # [1, 2, 3, 4, 5, 7]
    print(quick_sort([7, 3, 3, 4, 1]))     # [1, 3, 3, 4, 7]
    print(quick_sort([]))                  # []
    print(quick_sort([5, 5, 5, 5]))        # [5, 5, 5, 5]
