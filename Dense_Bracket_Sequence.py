for _ in range(int(input())):
    n = int(input())
    s = input()
    a,b = [0]*n,[0]*n
    for i in range(n):
        if s[i] == '(':
            a[i]+=1
        if i > 0:
            a[i] += a[i-1]
    ans = n+1

    for i in range(n-1,-1,-1):
        if s[i] == ')':
            b[i] += 1
        if i < n-1:
            b[i] += b[i+1]
        ans = min(ans,n-2*min(a[i],b[i]))
    print(ans)