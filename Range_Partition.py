for t in range(1,int(input())+1):
    n,x,y = map(int, input().split())
    
    print("Case #" + str(t) + ": ", end="")
    
    total = (n*(n+1))//2
    x = x+y
    if(total%x == 0):
        print("POSSIBLE")
        x = total//x
        y = y*x
        vc = [i for i in range(1, n+1)]
        for i in range(n-1, -1, -1):
            if vc[i] <= y:
                y = y - vc[i]
                vc[i] = 0
        vc = [i for i in vc if i != 0]
        print(len(vc))
        print(*vc)
    else:
        print("IMPOSSIBLE")