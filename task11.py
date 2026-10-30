def count_occurrences(arr, x):
    if len(arr) == 0:
        return 0
    if arr[0] == x:
        return 1 + count_occurrences(arr[1:], x)
    return count_occurrences(arr[1:], x)

print(count_occurrences([2, 5, 2, 8, 2, 9], 2))