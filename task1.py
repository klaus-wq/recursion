def power(N: int, M: int, res = 1) -> int | float:
    if M == 0:
        return res
    if M > 0:
        res = res * N
        M -= 1
    if M < 0:
        res = res * (1 / N)
        M += 1
    return power(N, M, res)

print(power(2, 0))
print(power(2, -3))
print(power(2, 3))