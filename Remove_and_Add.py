from collections import defaultdict
def solve(a):
    heap = defaultdict(int)
    count = n 
    j = 0
    for i in range(n):
        r,temp = n - i - 1,heap.get(a[i], 0)
        j = max(temp, j)
        heap[a[i]] = 1 + i
        count = min(count, min(j, r) + j + r)
    return count
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(a))