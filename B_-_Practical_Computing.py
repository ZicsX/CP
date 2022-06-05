n = int(input())
for i in range(n):
    a = 1
    print(a, end=' ')
    for j in range(i):
        a = a * (i - j) // (j + 1)
        print(a, end=' ')
    print()