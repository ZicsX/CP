for _ in range(int(input())):
    p = int(input())
    a, b = divmod(p, 100)
    print(a + b if a + b <= 10 else -1)