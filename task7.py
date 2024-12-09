def findMax(arr: list) -> int | None:
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    if arr[0] > arr[1]:
        max1 = arr[0]
        max2 = arr[1]
    else:
        max1 = arr[1]
        max2 = arr[0]
    return findSecondMax(arr, max1, max2, 2)

def findSecondMax(arr: list, max1: int, max2: int, index: int) -> int:
    if index == len(arr):
        return max2
    if arr[index] >= max1:
        max2 = max1
        max1 = arr[index]
    elif arr[index] > max2:
        max2 = arr[index]
    return findSecondMax(arr, max1, max2, index + 1)

print(findMax([15, 2, 70, 5, 11]))
print(findMax([15, 2, 70, 5, 70]))
print(findMax([15, 2, 456, 5, 70, 70]))
print(findMax([15, 2, 456, 5, 70, 70, 100000]))
print(findMax([70]))
print(findMax([]))