for _ in range(int(input())):
    N = int(input())
    if N == 1:
        print(3)
    else:
        S = int('1' + "0"*(N-2) + '1')
        E = int('9'*N)
        while S % 3 != 0 and E % 9 == 0:
            S += 2
        print(S)