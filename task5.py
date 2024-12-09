def printEvenElements(arr: list, index = 0):
    if len(arr) == index:
        return None
    if arr[index] % 2 == 0:
        print(arr[index])
    printEvenElements(arr, index + 1)

printEvenElements(([1, 4, 6, 3, 6]))
printEvenElements(([]))
printEvenElements([1])
printEvenElements([2000])