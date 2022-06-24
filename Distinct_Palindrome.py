for _ in range(int(input())):
    n,x = map(int,input().split())
    if x > n:
        print(-1)
    elif n == 1 and x == 1:
        print('a')
    elif n % 2 != 0:
        t = n//2
        if x > t+1:
            print(-1)
        else:
            s = ['a'] * n
            a = 'a'
            i = 0
            j = n-1
            ch = 1
            while i <= j:
                if i < j and ch <= x:
                    s[i] = a
                    s[j] = a
                    a = chr(ord(a)+1)
                    ch += 1
                elif i < j and ch > x:
                    a = 'a'
                    s[i] = a
                    s[j] = a
                    a = chr(ord(a)+1)
                    ch += 1
                elif i == j and ch <= x:
                    s[i] = a
                elif i == j and ch > x:
                    a = 'a'
                    s[i] = a
                i += 1
                j -= 1
            print(''.join(s))
            s = []
    else:
        t = n//2
        if x > t:
            print(-1)
        else:
            s = ['a'] * n
            a = 'a'
            i = 0
            j = n-1
            ch = 1
            while i <= j:
                if ch <= x:
                    s[i] = a
                    s[j] = a
                    a = chr(ord(a)+1)
                    ch += 1
                else:
                    a = 'a'
                    s[i] = a
                    s[j] = a
                    a = chr(ord(a)+1)
                    ch += 1
                i += 1
                j -= 1
            print(''.join(s))