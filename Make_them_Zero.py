t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    count=0
    while(1):
        maxx = max(l)
        if(maxx==0):
            break
        ind = maxx.bit_length()
        l = [x - 2**(ind-1) if x>=2**(ind-1) else x for x in l ]
        count+=1
    print(count)