for _ in range(int(input())):
    N = int(input())
    mex = list(map(int, input().split()))
    lower_bound = [0] * (N + 5)
    upper_bound = [0] * (N + 5)
    value = 0
    for i in range(N):
        b = N - mex[i]
        lower_bound[mex[i]] += 1
        upper_bound[mex[i]] += b
        value += b
    short = lower_bound
    for i in range(N, -1, -1):
        short[i] += short[i + 1]
    for i in range(N):
        y = value - upper_bound[i] + short[i + 1]
        x = short[i + 1]
        print(x, y)