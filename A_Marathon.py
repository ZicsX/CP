for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    print(sum([a < k for k in [b, c, d]]))