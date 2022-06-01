t = int(input())
for _ in range(t):

    n = int(input())
    a = list(map(int,input().split()))
    ans = (n*(n+1))//2
    inds = [[-1] for i in range(n+1)]
    for i,x in enumerate(a):
        inds[x].append(i)
    for i in range(1,n+1):
        inds[i].append(n)
        for j in range(1,len(inds[i])):
            l = inds[i][j]-inds[i][j-1]-1
            ans -= max(0,l-i+1)
    print(ans)