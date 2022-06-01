def max_geq_sum(arr):
    n = len(arr)
    if n == 1:
        return "YES"
    cum_sum = [0] * n
    cum_sum[0] = arr[0]
    for i in range(1, n):
        cum_sum[i] = cum_sum[i - 1] + arr[i]
    for i in range(1, n):
        mn = min(cum_sum[i - 1], cum_sum[n - 1] - cum_sum[i])
        mx = max(cum_sum[i - 1], cum_sum[n - 1] - cum_sum[i])
        if mx >= mn + arr[i]:
            return "YES"
    return "NO"
t=int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    print(max_geq_sum(arr))
