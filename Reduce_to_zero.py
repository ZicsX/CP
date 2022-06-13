for _ in range(int(input())):  
    x,y=map(int,input().split())
    if x==y:
        print(x)
        continue
    elif x==0 or y==0:
        print(-1)
        continue
    else:
        count=0
        if y<x:
            x,y=y,x
        while x*2<=y:
            x*=2
            count+=1
    if x>y:
        x/=2
        count-=1
    if x==y:
        print(count+x)
        continue
    if x<y:
        print(y+count+1)
        continue
    else:
        print(-1)
        continue