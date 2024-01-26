# 22:24
from copy import deepcopy
dirs = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
grid = []
num_dict = dict()

for _ in range(4):
    temp = list(map(int, input().split()))
    new_temp = []
    for i in range(4):
        new_temp.append([temp[i*2], temp[i*2+1]-1])
    grid.append(new_temp)

for y in range(4):
    for x in range(4):
        num, dir_num = grid[y][x]
        num_dict[num] = [x,y,dir_num]

temp_num, temp_dir = grid[0][0]
grid[0][0] = [0, temp_dir]
del num_dict[temp_num]
num_dict[0] = [0, 0, temp_dir]

def is_in(x, y):
    return 0 <= x < 4 and 0 <= y < 4

def fish_move(grid, num_dict):
    for i in range(1, 17):
        if i not in num_dict:
            continue
        x, y, dir_num = num_dict[i]
        for j in range(8):
            new_dir_num = (dir_num + j) % 8
            dx, dy = dirs[new_dir_num]
            nx, ny = x + dx, y + dy
            if not is_in(nx, ny):
                continue
            if grid[ny][nx] == []:
                grid[y][x][1] = new_dir_num
                num_dict[i] = [nx, ny, new_dir_num]
                grid[ny][nx], grid[y][x] = grid[y][x], []
                break
            target_num, target_dir = grid[ny][nx]
            if target_num == 0:
                continue
            grid[y][x][1] = new_dir_num
            num_dict[i] = [nx, ny, new_dir_num]
            num_dict[target_num] = [x, y, target_dir]
            grid[ny][nx], grid[y][x] = grid[y][x], grid[ny][nx]
            break
    return grid, num_dict

answer = 0

def shark_move(grid, num_dict, total_sum):
    global answer
    grid, num_dict = fish_move(grid, num_dict)
    x, y, dir_num = num_dict[0]
    moved = False
    for step in range(1, 4):
        nx, ny = x + dirs[dir_num][0] * step, y + dirs[dir_num][1] * step
        if not is_in(nx, ny) or grid[ny][nx] == []:
            continue
        moved = True
        new_grid = deepcopy(grid)
        new_num_dict = deepcopy(num_dict)
        temp_num, temp_dir = new_grid[ny][nx]
        new_grid[y][x] = []
        new_grid[ny][nx] = [0, temp_dir]
        new_num_dict[0] = [nx, ny, temp_dir]
        del new_num_dict[temp_num]
        shark_move(new_grid, new_num_dict, total_sum + temp_num)
    if not moved:
        answer = max(answer, total_sum)

shark_move(grid, num_dict, temp_num)
print(answer)