for i in range(int(input())):
    X, Y, Z = map(int, input().split())
    if(X*5+Y*10<Z):
        print("0")
    else:
        print((X*5+Y*10)//Z)