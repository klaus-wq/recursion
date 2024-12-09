def printEvenIndexes(arr: list, index = 0):
    if index >= len(arr):
        return None
    print(arr[index])
    printEvenIndexes(arr, index + 2)

printEvenIndexes(([1, 4, 6, 3, 6]))
printEvenIndexes(([]))
printEvenIndexes([1])
printEvenIndexes([2000])