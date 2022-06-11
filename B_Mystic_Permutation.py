for _ in range(int(input())):
    n = int(input())
    A = [int(x) for x in input().split()]
    P = [-1 for i in range(n + 1)]
    M = [0 for i in range(n + 1)]
    for i in range(1, n + 1):
        idx = -1
        for j in range(1, n + 1):
            if M[j] == 0:
                idx = j
                break
        if idx == -1:
            idx = n
        else:
            if A[i - 1] == idx and idx < n:
                idx = idx + 1
        P[i - 1] = idx
        M[idx] = 1
    if P[n - 1] == A[n - 1]:
        P[n - 1], P[n - 2] = P[n - 2], P[n - 1]
    print(*P[:-1])