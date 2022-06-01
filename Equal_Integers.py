for i in range(int(input())):
    x,y = map(int, input().split())
    if(x==y):
        print(0)
    elif(y>x):
        print(y-x)
    else:
        if((x-y)%2==0):
            print((x-y)//2)
        else:
            print(int(((x-y)+1)/2)+1)
