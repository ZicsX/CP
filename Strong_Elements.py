from math import gcd as g
def GCD(l, r, s, e, n):
  if l == 0:
    return e[r + 1]
  if r == n - 1:
    return s[l - 1]
  return g(s[l - 1], e[r + 1])

for _ in range(int(input())):
  n = int(input())
  s = [0] * n
  e = [0] * n
  
  
  A = list(map(int,input().split()))
  s[0] = A[0]

  for i in range(1, n):
    s[i] = g(s[i - 1], A[i])

  e[n - 1] = A[n - 1]

  for i in range(n - 2, -1, -1):
    e[i] = g(e[i + 1], A[i])

  count = 0

  for i in range(n):
    if GCD(i, i, s, e, n) > 1:
      count += 1
   
  print(count)