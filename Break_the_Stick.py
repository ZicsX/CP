for _ in range(int(input())):
    n,x = map(int,input().split())
    if(n%2 != 0 and x%2== 0):
        print("NO")
    else:
        print("YES")