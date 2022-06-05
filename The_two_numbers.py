for _ in range(int(input())):
    n = int(input())
    if n == 2:
        print(0)
    elif n % 2 != 0:
        print((int(n / 2) * int(n / 2 + 1)) - 1)
    else:
        if (n / 2) % 2 == 0:
            print(((int(n / 2) - 1) * (int(n / 2) + 1)) - 1)
        else:
            print(((int(n / 2) - 2) * (int(n / 2) + 2)) - 1)