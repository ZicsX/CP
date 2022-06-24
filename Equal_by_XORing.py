import math

def countBits(number):
    return (math.log2(number))+1
def isPowerOfTwo(n):
    return math.ceil(math.log2(n) == math.floor(math.log2(n)))
    
for _ in range(int(input())):
    a,b,n = map(int,input().split())
    x = a ^ b
    if(a == b):
        print(0)
    elif(x < n):
        print(1)
    else:
        d1 = countBits(x)
        d2 = countBits(n)
        if(d1 == d2):
            print((-1 if isPowerOfTwo(n) else 2))
        else:
            print(-1)