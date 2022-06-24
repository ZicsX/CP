mod=1e9+7
p=[]
x=1
increment =2
sq=0
while(x<=1e9):
  p.append(x)
  x+=increment 
  increment +=1
psum=[]
qsum=[]
sq=0
x=0
for i in p:
  x+=i
  x%=mod
  sq+=(i*i)%mod
  sq%=mod
  psum.append(x)
  qsum.append(sq)
for _ in range(int(input())):
  n=int(input())
  id=len(list(filter(lambda i: i<n,p)))
  if id==0:
    print(0)
  else:
    print(int(((n*psum[id-1])%mod-qsum[id-1]+mod)%mod))