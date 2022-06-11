import math

def lightItUp(N, K, A, X, Y):

    min_strength = 0

    for i in range(N):
        lit = False
        for j in range(K):
            if math.sqrt((X[A[j]-1]-X[i])**2 + (Y[A[j]-1]-Y[i])**2) <= min_strength:
                lit = True
                break
        if not lit:
            min_strength = math.sqrt((X[A[j]-1]-X[i])**2 + (Y[A[j]-1]-Y[i])**2)

    return min_strength

N, K = map(int,input().split())
A = list(map(int,input().split()))
X = []
Y = []
for i in range(N):

    x, y = map(int,input().split())
    X.append(x)
    Y.append(y)

print('{0:.12f}'.format(lightItUp(N, K, A, X, Y)))
