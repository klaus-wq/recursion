def sum(N: int, res = 0) -> int:
    if N == 0:
        return res
    return sum(N // 10, res + N % 10)

print(sum(0))
print(sum(10))
print(sum(123456))