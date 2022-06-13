for _ in range(int( input())):

    n = int(input())
    p = list(range(1,n+1))
    a = [0]*n
    
    for i in range((n//2)+1):
        if (n-2*i-1) >= 0: a[n-2*i-1] = p[n-i-1]
        if (n-2*i-2) >= 0: a[n-2*i-2] = p[i]
    print(*a)