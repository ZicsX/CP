for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    d=[]
    d.append(b[0]-a[0])
    f=b[0]
    for i in range(1,n):
        f=max(f,a[i],b[i-1])
        d.append(max(0,b[i]-f))
    for i in d:
        print(i, end=' ')
    print()


