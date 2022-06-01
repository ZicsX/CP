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


# from collections import defaultdict

# for _ in range(int(input())):
#     n = int(input())
#     a = list(map(int, input().split()))
#     h = defaultdict(int)
#     c = n 
#     j = 0
#     for i in range(n):
#         if a[i] in h:
#             t = h[a[i]]
#         else:
#             t = 0
#         j = max(t, j)
#         h[a[i]] = 1 + i
#         c = min(c, min(j, n-i-1) + j + n-i-1)
#     print(c)