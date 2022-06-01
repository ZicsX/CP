for _ in range(int(input())):
    N, K = map(int, input().split())
    if N % 2 == 0:
        print('Yes')
    elif K==1:
        print('Yes')
    else:
        print('No')