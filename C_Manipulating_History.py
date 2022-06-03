for _ in range(int(input())):
  n = int(input())
  ll = [0] * (2*n)
  for i in range(2*n):
    ll[i] = input()
  s = input()
  m = {}
  for i in range(len(s)):
    if s[i] in m:
      m[s[i]] += 1
    else:
      m[s[i]] = 1
  for i in range(2*n):
    for j in range(len(ll[i])):
      if ll[i][j] in m:
        m[ll[i][j]] += 1
      else:
        m[ll[i][j]] = 1
  ans = 0
  for key in m:
    if m[key] % 2 != 0:
      ans = key
  print(ans)