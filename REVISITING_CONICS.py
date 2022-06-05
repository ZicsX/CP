for _ in range(int(input())):
    D,A,B=map(int,input().split())
    if D==0:
        if A==B:
            print(-1)
        else:
            print(0)
    elif D>A+B:
        print(0)
    elif D==A+B:
        print(1)
    else:
        print(2)