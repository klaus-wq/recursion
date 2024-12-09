def palindrom(string: str, first: int, last: int) -> bool:
    if len(string) == 0 or len(string) == 1:
        return True
    if first >= last:
        return True
    if string[first] != string[last]:
        return False
    return palindrom(string, first + 1, last - 1)

print(palindrom('', 0, len('') - 1))
print(palindrom('4', 0, len('4') - 1))
print(palindrom('1221', 0, len('1221') - 1))
print(palindrom('12r21', 0, len('12r21') - 1))
print(palindrom('dfgdgdfg', 0, len('dfgdgdfg') - 1))