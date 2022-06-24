def floor(c,f): 
    return abs((f-c)//10)

for _ in range(int(input())):
 x,y=map(int,input().split())
 
 print(floor(x,y))