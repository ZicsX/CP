for _ in range(int(input())):
    x = int(input())
    B = bin(x)[2:]
    if x == 1 or x == 2:
        print(3)
        continue
    print(x+1 if B.count('1') == 1 else 2**(len(B)-1-B.rindex('1')))