def find_max(arr):
    if len(arr) == 1:
        return arr[0]
    rest_max = find_max(arr[1:])
    return arr[0] if arr[0] > rest_max else rest_max

print(find_max([4, 8, 2, 15, 7]))