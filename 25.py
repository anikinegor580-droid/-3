def count_inversions(arr):
    def merge_sort_and_count(sub_arr):
        if len(sub_arr) <= 1:
            return sub_arr, 0
        mid = len(sub_arr) // 2
        left, inv_left = merge_sort_and_count(sub_arr[:mid])
        right, inv_right = merge_sort_and_count(sub_arr[mid:])
        merged = []
        i = j = 0
        inv_split = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv_split += len(left) - i
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv_left + inv_right + inv_split
    _, total_inversions = merge_sort_and_count(arr)
    return total_inversions
if __name__ == "__main__":
    print(count_inversions([1, 2, 3]))        # 0
    print(count_inversions([3, 2, 1]))        # 3
    print(count_inversions([2, 4, 1, 3, 5]))  # 3
    print(count_inversions([5, 4, 3, 2, 1]))  # 10
