for _ in range(int(input())):
  N, Q = map(int, input().split())
  S = input()
  arr = list(map(int, input().split()))
  
  M = {}
  for i in range(N):
    M[arr[i]] = i+1

  ranges = [list(map(int, input().split())) for i in range(Q)]
  ranges.sort()
  
  m = [ranges[0]]
  for i in range(1, Q):
    if ranges[i][0] > m[-1][1]:
      m.append(ranges[i])
    else:
      pt = m[-1]
      m.pop()
      m.append((pt[0], max(ranges[i][1], pt[1])))

  A = 0
  for i in range(len(m)):
    pre = 0
    c = {}
    for j in range(m[i][0]-1, m[i][1]):
      c[S[j]] = c.get(S[j], 0) + 1

    rg = []
    for j in range(m[i][0]-1, m[i][1]):
      rg.append((M[j+1], S[j]))
    rg.sort()
    while rg:
      start = rg.pop(0)
      if c[start[1]] > 1:
        c[start[1]] -= 1
        A += (start[0] - pre)
        pre = start[0]

  print(A)