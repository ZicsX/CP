t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().rstrip().split()))
    ec = 0
    oc = 0
    for i in range(n):
        if a[i]%2 == 0:
            ec +=1 
        else:
            oc +=1
    if oc == 0 or ec == 0:
        print(0)
    else:
        print(min(ec,oc))