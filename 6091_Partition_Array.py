def partitionnumsay(nums, k):
    nums.sort(reverse=True)
    n = len(nums)

    s = nums[0]
    c = 0

    for i in range(n):
        if s - nums[i] > k:
            s = nums[i]
            c += 1
    c = c + 1
    return c

nums = [3,6,1,2,5]
k = 2
print(partitionnumsay(nums, k))