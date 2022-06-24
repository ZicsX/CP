t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    first = a[0]
    for i in range(1,n):
        if a[i] >= first:
            first = a[i]
        else:
            print("No")
            break
    else:
        print("Yes")