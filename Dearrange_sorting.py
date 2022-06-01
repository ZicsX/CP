def minimumOperations(N, P):
    operations = 0
    for i in range(1,N):
        if P[i] < P[i-1]:
            operations += 1
            for j in range(i,N):
                if P[j] < P[i-1]:
                    P[j], P[i-1] = P[i-1], P[j]
                    operations += 1
                else:
                    break
    return operations

for _ in range(int(input())):
    N = int(input())
    P = list(map(int, input().split()))
    print(minimumOperations(N, P))