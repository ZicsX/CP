h,w = map(int,input().split())
grid = [list(input().strip()) for x in range(h)]


for i in range(h):
    for j in range(w):
        if grid[i][j] == 'o':
            first_piece = [i,j]
            break

for i in range(h):
    for j in range(w):
        if grid[i][j] == 'o':
            if [i,j] != first_piece:
                second_piece = [i,j]
                break

dx = abs(first_piece[0]-second_piece[0])
dy = abs(first_piece[1]-second_piece[1])

for i in range(h):
    for j in range(w):
        if grid[i][j] == 'o':
            if [i,j] != first_piece and [i,j] != second_piece:
                dx = abs(first_piece[0]-i)
                dy = abs(first_piece[1]-j)

print(dx+dy)