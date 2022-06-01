for i in range(int(input())):
  A = list(map(int, input().split()))
  P = max(A[0] , A[1])
  Q = max(A[2] , A[3])
  if P < Q:
    print("P")
  elif Q < P:
    print("Q")
  else:
    print("TIE")