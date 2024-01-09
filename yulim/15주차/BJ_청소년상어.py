import copy

maps = [[] for _ in range(4)]
for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(0, 8, 2):
        maps[i].append([tmp[j], tmp[j+1]-1]) #방향은 -1을 해준다.

dv = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

def dfs(sx, sy, fish_count, maps):
    global max_fish_count
    fish_count += maps[sx][sy][0]
    max_fish_count = max(max_fish_count, fish_count)
    maps[sx][sy][0] = -1

    for f in range(1, 17):
        fx, fy = -1, -1
        for x in range(4):
            for y in range(4):
                if maps[x][y][0] == f:
                    fx, fy = x, y
                    break
        if fx == -1 and fy == -1:
            continue
        fd = maps[fx][fy][1]

        for i in range(8):
            nd = (fd+i) % 8
            nx = fx + dv[nd][0]
            ny = fy + dv[nd][1]
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                continue
            maps[fx][fy][1] = nd
            maps[fx][fy], maps[nx][ny] = maps[nx][ny], maps[fx][fy]
            break


    sd = maps[sx][sy][1]
    nx, ny = sx, sy
    while True:
        nx += dv[sd][0]
        ny += dv[sd][1]
        if nx < 0 or nx >= 4 or ny < 0 or ny >= 4: return
        elif maps[nx][ny][0] == -1: continue
        dfs(nx, ny, fish_count, copy.deepcopy(maps))

max_fish_count = 0
dfs(0, 0, 0, maps)
print(max_fish_count)
