for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    maxSum = A[0] + A[N-1]
    i = 0
    j = -1
    for tt in range(N-1):
        if A[i] + A[j] > maxSum:
            maxSum = A[i] + A[j]
        i-= 1
        j-= 1
    print(maxSum)