def Factors(n): 

    count = 0

    i = 1
    while (i * i < n):
        if (n % i == 0):
            count+=1
        i += 1

    for i in range(int(n**0.5), 0, -1):
        if (n % i == 0):
            count+=1
    return count

for _ in range(int(input())):  
    a,b = map(int,input().split())
    print(Factors(abs(b-a)))