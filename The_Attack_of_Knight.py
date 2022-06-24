def isValid(x, y):
    return x >= 1 and x <= 8 and y >= 1 and y <= 8

def check(x1, y1, x2, y2):
    arr1 = [-1, 1, 2, 2, 1, -1, -2, -2]
    arr2 = [-2, -2, -1, 1, 2, 2, 1, -1]
    for i in range(8):
        for j in range(8):
            if isValid(x1 + arr1[i], y1 + arr2[i]) and isValid(x2 + arr1[j], y2 + arr2[j]):
                if x1 + arr1[i] == x2 + arr1[j] and y1 + arr2[i] == y2 + arr2[j]:
                    return True
    return False

for _ in range(int(input())):
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    if check(x1, y1, x2, y2):
        print("YES")
    else:
        print("NO")