def palindrom(string: str) -> bool:
    if len(string) == 0 or len(string) == 1:
        return True
    return check(string, 0, len(string) - 1)

def check(string: str, first: int, last: int):
    if first >= last:
        return True
    if string[first] != string[last]:
        return False
    return check(string, first + 1, last - 1)

print(palindrom(''))
print(palindrom('4'))
print(palindrom('1221'))
print(palindrom('12r21'))
print(palindrom('dfgdgdfg'))