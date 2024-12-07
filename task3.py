def lenOfList(arr: list) -> int:
    if len(arr) == 0:
        return 0
    arr.pop(0)
    return lenOfList(arr) + 1

print(lenOfList([1, 4, 6, 7]))
print(lenOfList([1]))
print(lenOfList([]))