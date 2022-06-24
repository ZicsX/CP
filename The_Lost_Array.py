for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    c=[]
    xor = 0
    for i in A:
        xor^=i
    if(n%2==1):
        flag=True
        for i in A:
            if(i^xor==0 and flag==True):
                flag = False
                continue
            c.append(i^xor)
    else:
        for i in A:
            xor^=i
            if(xor!=0):
                break
        flag = True
        for i in A:
            if (i ^ xor == 0 and flag == True):
                flag = False
                continue
            c.append(i ^ xor)
    print(*c)