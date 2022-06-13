from math import gcd 
def D(ind,par,dics,arr,inter,final):
    counts = arr[ind]
    sum=0
    for i in dics[ind]:
        if(i!=par):
            curr = D(i,ind,dics,arr,inter,final)
            sum+=curr
            counts = gcd(counts,curr)
    inter[ind]=counts
    final[ind]=sum
    return counts
def F(ind,par,su,dics,arr,inter,final,count):
    count = max(count,su)
    for i in dics[ind]:
        if(i!=par): 
            count = F(i,ind,su-inter[i]+final[i],dics,arr,inter,final,count)
    return count
for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    inter = [0 for i in range(n)]
    final = [0 for i in range(n)]
    count=0
    dics = {i:[] for i in range(n)}
    for i in range(n-1):
        x,y = map(int,input().split())
        x-=1
        y-=1
        dics[x].append(y)
        dics[y].append(x)
    count = D(0,-1,dics,arr,inter,final)
    couunt = F(0,-1,final[0],dics,arr,inter,final,count)
    print(count)