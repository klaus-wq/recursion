def printEvenElements(arr: list):
    return check(arr, 0)

def check(arr: list, index: int):
    if len(arr) == index:
        return None
    if arr[index] % 2 == 0:
        print(arr[index])
    check(arr, index + 1)

printEvenElements(([1, 4, 6, 3, 6]))
printEvenElements(([]))
printEvenElements([1])
printEvenElements([2000])