def provinces(n, land, water): 
    global visited_land, visited_water
    visited_land = [False] * (n+1) 
    visited_water = [False] * (n+1) 
    for i in range(len(land)): 
        for j in range(2): 
            if visited_land[land[i][j]] == False: 
                dfs_land(land[i][j], visited_land, land, water) 
    count = 0
    for i in range(1, n+1): 
        if visited_land[i] == True and visited_water[i] == False: 
            count += 1
    print(count) 
def dfs_land(i, visited_land, land, water): 
    stack = [] 
    stack.append(i) 
    while(len(stack)): 
        s = stack[-1] 
        stack.pop() 
        if visited_land[s] == False: 
            visited_land[s] = True
            for j in range(len(land)): 
                if land[j][0] == s: 
                    stack.append(land[j][1]) 
                if land[j][1] == s: 
                    stack.append(land[j][0]) 
            for j in range(len(water)): 
                if water[j][0] == s: 
                    visited_water[water[j][1]] = True
                if water[j][1] == s: 
                    visited_water[water[j][0]] = True
t = int(input()) 
for _ in range(t): 
    n = int(input()) 
    land = [] 
    water = [] 
    a, b = map(int, input().split()) 
    for i in range(a): 
        land.append(list(map(int, input().split()))) 
    for i in range(b): 
        water.append(list(map(int, input().split()))) 
    provinces(n, land, water)