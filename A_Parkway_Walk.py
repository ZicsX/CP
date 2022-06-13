for _ in range(int(input())):
    n,m = map(int, input().rstrip().split())
    A = [int(i) for i in input().split()]
    summ = sum(A)
    summ = summ - m if summ > m else 0
    print(summ)