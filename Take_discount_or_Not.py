for _ in range(int(input())):
    N, X, Y = map(int,input().split())
    A = list(map(int,input().split()))
    T = sum(A)
    coupon = X + sum([0 if a<=Y else a-Y for a in A])
    print('COUPON' if coupon<T else 'NO COUPON')