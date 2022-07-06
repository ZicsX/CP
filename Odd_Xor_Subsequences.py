# from itertools import combinations

# def solve(numbers, k):
#     return sum(1 for subset in combinations(numbers, k) if sum(subset) & 1)

# N = int(input())
# A = list(map(int, input().split()))
# for _ in range(int(input())):
#     K = int(input())
#     print(solve(A,K))


def oddSubsequences(A, K):
    return oddSubsequencesUtil(A, K, 0, 0)

def oddSubsequencesUtil(A, K, currIdx, sumSoFar):

    if sumSoFar % 2 == 1 and K == 0:
        return 1

    if K == 0:
        return 0

    if currIdx == len(A):
        return 0

    if (currIdx, sumSoFar, K) in dp:
        return dp[(currIdx, sumSoFar, K)]

    include = oddSubsequencesUtil(A, K - 1, currIdx + 1, sumSoFar + A[currIdx])
    exclude = oddSubsequencesUtil(A, K, currIdx + 1, sumSoFar)

    dp[(currIdx, sumSoFar, K)] = include + exclude
    return include + exclude


dp = {}
N = int(input())
A = list(map(int, input().split()))
for _ in range(int(input())):
    K = int(input())
    print(oddSubsequences(A, K))
