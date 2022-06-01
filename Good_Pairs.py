import collections

for _ in range(int(input())):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    d = collections.defaultdict(int)
    
    count = 0
    for i in range(N):
        u = A[i] ^ B[i]
        count += d[u]
        d[u] += 1
    print(count)