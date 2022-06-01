n = int(input())
s = []
for i in range(n):
    t = list(map(int, input().split()))
    if t[0] == 1:
        s.append(t[1])
    elif t[0] == 2:
        for j in range(min(t[2], s.count(t[1]))):
            s.remove(t[1])
    else:
        print(max(s) - min(s))