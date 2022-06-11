def solve(a, b, k): 
    
    res = "" 
    c1 = c2 = 0
    i, j = 0, 0
    n, m = len(a), len(b) 
    a = sorted(a) 
    b = sorted(b) 
    
    while i < n and j < m: 
        if a[i] < b[j] and c1 < k: 
            res += a[i] 
            i += 1
            c1 += 1
            c2 = 0
        elif a[i] > b[j] and c2 < k: 
            res += b[j] 
            j += 1
            c2 += 1
            c1 = 0
        elif c1 < k: 
            res += a[i] 
            i += 1
            c1 += 1
            c2 = 0
        elif c2 < k: 
            res += b[j] 
            j += 1
            c2 += 1
            c1 = 0
    return res 
    
for _ in range(int(input())):
    n, m, k = map(int, input().split())
    a = input()
    b = input()
    print(solve(a, b, k))