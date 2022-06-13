for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    d = {}
    for i in range(n):
        if a[i] != b[i]:
            d[b[i]] = True
    print(len(d))