def is_square(num):
    return num**0.5 == int(num**0.5)

N = int(input())

squares = 0
for i in range(1, N+1):
    for j in range(1,N+1):
        if is_square(i*j):
            squares+=1
print(squares)