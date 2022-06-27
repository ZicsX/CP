import collections as C
def root(x, g):
    if x != g[x]:
        g[x] = root(g[x], g)
    return g[x]

def solve(N, A, B, land, water):
    l, w = list(range(N+1)), list(range(N+1))
    for i, j in land:
        l[root(i, l)] = l[root(j, l)]

    for i, j in water:
        w[root(i, w)] = w[root(j, w)]

    capture = C.Counter(root(i, l) for i in range(1, N+1))
    c = C.defaultdict(C.Counter)

    for i in range(N+1):
        i, j = root(i, l), root(i, w)
        c[i][j] += 1
        if c[i][j] > 1:
            capture[i] = 0

    return max(capture.values())
    
for _ in range(int(input())):
    N = int(input())
    A = int(input())
    B = int(input())
    land = [list(map(int, input().split())) for i in range(A)]
    water = [list(map(int, input().split())) for i in range(B)]

    out_ = solve(N, A, B, land, water)
    print (out_)