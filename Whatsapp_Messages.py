T = int(input())
for i in range(T):
   N = int(input())
   l = list(map(int,input().split()))
   flag = 0
   for j in range(N-1):
      if l[j]>l[j+1]:
         flag = 1
   if flag == 0:
      print("YES")
   else:
      print("NO")