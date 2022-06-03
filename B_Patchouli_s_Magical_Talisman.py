import sys
MAX_INT = sys.maxsize

for _ in range(int(input())):
  n = int(input())
  a = list(map(int, input().split()))
  Mag = 0
  for i in range(0, n):
    if(a[i] & 1):
      Mag += 1
  if(Mag):
    print(n - Mag)
  else:
    M = MAX_INT
    for i in range(0, n):
      val = a[i]
      c = 0
      while(a[i] % 2 == 0):
        a[i] /= 2
        c += 1
      M = min(M, c)
    print(M + n - 1)