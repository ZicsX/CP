# def win(power,n):
#     el = 0
#     vc = 0
#     while (n > 0): 
#         if (power[0] < power[n - 1]): 
#             el = el + power[0] 
#             power.pop(0) 
#         else: 
#             el = el + power[n - 1] 
#             power.pop(n - 1) 
#         n = n - 1
#         if (n == 0): 
#             break
#         if (power[0] < power[n - 1]): 
#             vc = vc + power[0] 
#             power.pop(0) 
#         else: 
#             vc = vc + power[n - 1] 
#             power.pop(n - 1) 
#         n = n - 1
#     if (el == vc): 
#         return 1
#     else: 
#         return 0

# power = list(map(int,input().split()))
# n = len(power)
# print(win(power,n))