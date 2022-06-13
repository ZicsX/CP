for _ in range(int(input())):  
    a, b = map(int, input().split())
    if (b-a)%3 == 2:
       print("NO")
    else:
       print("YES")
