T = int(input())
 
for i in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    
    X = 0
    for j in range(N):
        X = X | A[j]
         
    for j in range(N):
        X = X | B[j]
         
    print(X)