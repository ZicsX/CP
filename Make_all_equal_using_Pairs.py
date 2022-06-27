for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    d = {}
    m = -1
    s = 0

    for i in range(n):
        if A[i] in d:
            d[A[i]] += 1
        else:
            d[A[i]] = 1

    for i in d:
        m = max(d[i], m)
        s += d[i]
        
    print(s - m)