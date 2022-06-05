# n,k=map(int,input().split())
# a=list(map(int,input().split()))

# a.sort()

# for i in range(n-1):
#     if abs(a[i]-a[i+1]) == k:
#         print("Yes")
#         break
# else:
#     print("No")


# def k_swap(a,n,k):
#     for i in range(n-k):
#         if i + k >= n:
#             break
#         if a[i] <= a[i + k]: 
#             continue
#         a[i], a[i + k] = a[i + k], a[i]

#     if sorted(a) == a:
#         return True
#     return sorted(a) == a

# n,k=map(int,input().split())
# a=list(map(int,input().split()))

# if k_swap(a,n,k):
#     print("Yes")
# else:
#     print("No")

# def issorted(A):
#     N = len(A)
#     K = 1
#     maximum = A[0]
 
#     for i in range(1, N):
#         if A[i] > maximum:
#             # current value is in the wrong position
#             # swap it with the maximum value
#             A[i], A[maximum_index] = A[maximum_index], A[i]
 
#         maximum = max(maximum, A[i])
 
#     return A == sorted(A)
 
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
 
# if issorted(A):
#     print('Yes')
# else:
#     print('No')