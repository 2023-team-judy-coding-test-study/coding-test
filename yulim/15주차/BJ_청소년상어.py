
import copy

maps = [[] for _ in range(4)]
for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(0, 8, 2):
        maps[i].append((tmp[j], tmp[j+1]-1)) #방향은 -1을 해준다.

dv = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def fishMove(maps):
    new_maps = copy.deepcopy(maps)

    fishes = [(-1, -1)]*17
    for i in range(4):
        for j in range(4):
            if new_maps[i][j][0] != 100:
                fishes[new_maps[i][j][0]] = (i,j)

    for i in range(1, 17):
        
        x, y = fishes[i]
        if x == -1: continue

        fish, d = new_maps[x][y]

        for _ in range(8):
            nx = x + dv[d][0]
            ny = y + dv[d][1]

            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4 or new_maps[nx][ny][0] == 100:
                d = (d + 1) % 8 # 반시계 방향으로 45도 회전
                continue
            elif new_maps[nx][ny][1] == -1:         # 빈칸이라면 이동
                new_maps[nx][ny] = (fish, d)
                new_maps[x][y] = (-1, -1)
                break
            else:                           # 빈칸이 아니라면 다른 칸 물고기와 위치 교환
                tmp_fish, tmp_d = new_maps[nx][ny]  # 이동할 곳의 물고기 정보 받기
                new_maps[nx][ny] = (fish, d)        # 이동할 물고기 이동
                new_maps[x][y] = (tmp_fish, tmp_d)  # 원래 있던 물고기 이동
                fishes[tmp_fish] = (x, y)       # fishes 리스트의 tmp_fish 정보 수정
                break

    return new_maps


def sharkMove(shark_x, shark_y, fish_x, fish_y, maps, fish_count):
    new_maps = copy.deepcopy(maps)

    fish, d = new_maps[fish_x][fish_y]
    fish_count += fish
    new_maps[shark_x][shark_y] = (-1, -1)
    new_maps[fish_x][fish_y] = (100, d)

    return new_maps, fish_count
    

def dfs(shark_x, shark_y, maps, fish_count):
    global max_fish_count

    tmp_shark_x, tmp_shark_y = shark_x, shark_y

    while True:
        d = maps[shark_x][shark_y][1]
        tmp_shark_x += dv[d][0]
        tmp_shark_y += dv[d][1]

        if tmp_shark_x < 0 or tmp_shark_x >= 4 or tmp_shark_y < 0 or tmp_shark_y >= 4: # 범위를 벗어나면
            max_fish_count = max(max_fish_count, fish_count)
            return

        elif maps[tmp_shark_x][tmp_shark_y][0] == -1 or maps[tmp_shark_x][tmp_shark_y][0] == 100: # 가려는 곳에 물고기가 없으면
            continue
        
        else: # 가려는 곳에 물고기가 있으면
            new_maps, new_fish_count = sharkMove(shark_x, shark_y, tmp_shark_x, tmp_shark_y, maps, fish_count)
            dfs(tmp_shark_x, tmp_shark_y, fishMove(new_maps), new_fish_count)


maps, max_fish_count = sharkMove(0,0,0,0,maps,0) # 상어의 첫 이동
maps = fishMove(maps) # 물고기 이동
dfs(0, 0, maps, max_fish_count)
print(max_fish_count)


"""
16 7 1 4 4 3 12 8
14 7 7 6 3 4 10 2
5 2 15 2 8 3 6 4
11 8 2 4 13 5 9 4

"""
