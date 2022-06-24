def optimal(n) : 
    count = 0
    for i in range(1, int(n**0.5) + 1): 
        if (n % i == 0) : 
            if (n // i == i) : 
                count = count + 1
            else : 
                count = count + 2 
    return count 
  
for _ in range(int(input())):  
    n = int(input()) 
    count = (optimal(n) - 1) * 2
    if (n % 2 == 0) : 
        count = count - 1
    print(count) 
