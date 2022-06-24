for _ in range(int(input())):
    n, x = map(int, input().split())
    p = int(1e9+7)
    result = 1
    xor = 2
    y = n - 1
    xor = xor % p
    while y > 0:
        if y & 1:
            result = (result * xor) % p
        y = y >> 1
        xor = (xor * xor) % p
    calories = (result % p * x % p) % p
    print(calories)