for i in range(int(input())):
    n, k = map(int, input().split())
    if k == 1:
        print("EVEN" if n%2 == 0 else "ODD")
    else:
        print("ODD" if k == 2 else "EVEN")
