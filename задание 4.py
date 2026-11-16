def insertion_sort(arr):
    result = arr.copy()
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1
        result[j + 1] = key
        
    return result
if __name__ == "__main__":
    original = [4, 2, 7, 1, 3, 5]
    print(insertion_sort(original))        # [1, 2, 3, 4, 5, 7]
    print(original)                        # [4, 2, 7, 1, 3, 5] (не изменился)
    print(insertion_sort([7, 3, 3, 4, 1])) # [1, 3, 3, 4, 7]
    print(insertion_sort([]))              # []
