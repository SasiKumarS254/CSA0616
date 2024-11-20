def merge_sort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return sorted(left + right)
print(merge_sort([38, 27, 43, 3, 9, 82, 10]))
