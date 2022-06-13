def solve():
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    k = False
    while a[0] >= b[0]:
        for i in range(n):
            if a[i] == 0:
                continue
            a[i] -= 1
        k = True
    j = True
    for i in range(n):
        if a[i] != b[i]:
            j = False
            break
    if j and k:
        print("YES")
    else:
        print("NO")
for _ in range(int(input())):
    solve()