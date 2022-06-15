for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    s = set(A)
    if((n-len(s))%2):
        print(len(s)-1)
    else:
        print(len(s))