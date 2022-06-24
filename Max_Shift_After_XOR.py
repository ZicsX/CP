for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = [a[0]]
    for i in range(1, n):
        b.append(b[i-1] ^ a[i])
    value = len(set(b))
    for i in range(n):
        a[i] = a[i] ^ b[-1]
        b[i] = a[i]
        value = max(value, len(set(b)))
    print(value) 