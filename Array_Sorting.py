for _ in range(int(input())):
    n = int(input())
    arr = {}
    v = list(map(int, input().split()))
    for i in range(n):
        arr[v[i]] = i
    arr = sorted(arr)
    res = []
    ans = 0
    for i in range(n-1,-1,-1):
        x = arr[i][1]
        while(x<(arr[i][0]-1)):
            ans += 1
            y = v[x+1]
            v[x] = y
            arr[y-1][1] = x
            res.append([x+1,x+1+1])
            x += 1
    print(ans)
    for i in range(res):
        print(res[i][0],res[i][1])
