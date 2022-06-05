def SIMPLE_XOR(l, r):
    for i in range(l, r+1):
        for j in range(i+1, r+1):
            for k in range(j+1, r+1):
                temp=(i^j^k)
                if(temp>=l and temp<=r):
                    s=set([i,j,k,temp])
                    if(len(s)==4):
                        return s
    return set()

for _ in range(int(input())):
    l,r=map(int, input().split())
    s=SIMPLE_XOR(l,r)
    if(len(s)==0):
        print(-1)
    else:
        print(*s)