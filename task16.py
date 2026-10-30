def subsets(arr, start, current, result):
    result.append(current[:])
    for i in range(start, len(arr)):
        current.append(arr[i])
        subsets(arr, i + 1, current, result)
        current.pop()

result = []
subsets([1, 2, 3], 0, [], result)
result.sort(key=len)
for s in result:
    print(s)