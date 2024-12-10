def printEvenIndexes(arr: list):
    return check(arr, 0)

def check(arr: list, index: int):
    if index >= len(arr):
        return None
    print(arr[index])
    check(arr, index + 2)

printEvenIndexes(([1, 4, 6, 3, 6]))
printEvenIndexes(([]))
printEvenIndexes([1])
printEvenIndexes([2000])