def palindrom(string: str) -> bool:
    if len(string) == 0 or len(string) == 1:
        return True
    if string[0] == string[-1]:
        return palindrom(string[1:-1])
    return False

print(palindrom(''))
print(palindrom('4'))
print(palindrom('1221'))
print(palindrom('12r21'))
print(palindrom('dfgdgdfg'))