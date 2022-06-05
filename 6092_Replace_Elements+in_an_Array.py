def arrayChange(nums, operations):
    m = {}
    for i in range(len(nums)):
        m[nums[i]] = i
    for i in range(len(operations)):
        idx = m[operations[i][0]]
        m[operations[i][0]] = 0
        nums[idx] = operations[i][1]
        m[operations[i][1]] = idx
    return nums

nums = [1,2,4,6]; operations = [[1,3],[4,7],[6,1]]
print(arrayChange(nums, operations))
nums = [1,2]; operations = [[1,3],[2,1],[3,2]]
print(arrayChange(nums, operations))