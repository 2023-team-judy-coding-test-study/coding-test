# 3:26 ~ 5:20 (1'54")
# python3 - 시간 초과
# pypy3 - 맞았습니당

from collections import deque

def findFishes(shark_size):
    global N
    fishes = []
    x, y = -1, -1
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 9:
                x = i
                y = j

            elif maps[i][j] < shark_size and maps[i][j] != 0:
                fishes.append((i, j))
    return fishes, x, y


def bfs(now_x, now_y, pos_x, pos_y, N, shark_size):
    queue = deque()
    queue.append((now_x, now_y, 0))

    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[now_x][now_y] = 1

    min_distance = 1e9
    
    while queue:
        
        x, y, m = queue.popleft()

        if x == pos_x and y == pos_y:
            min_distance = min(min_distance, m)

        for d in dv:
            nx = x + d[0]
            ny = y + d[1]

            if nx < 0 or nx >= N or ny < 0 or ny >= N or maps[nx][ny] > shark_size or visited[nx][ny] == 1:
                continue
            elif maps[nx][ny] <= shark_size:
                visited[nx][ny] = 1
                queue.append((nx, ny, m+1))
                
    return min_distance

N = int(input())
maps = [[int(x) for x in input().split()] for _ in range(N)]
dv = [(-1, 0), (0, -1), (1, 0), (0, 1)]


fish_count = 0
move_count = 0
shark_size = 2
while True:
    fishes, shark_x, shark_y = findFishes(shark_size)

    if len(fishes) == 0:    # 먹을 수 있는 물고기가 없으면
        break

    else:
        distance = 1e9
        fish_x, fish_y = -1, -1          

        for i, j in fishes: 
            tmp_distance = bfs(shark_x, shark_y, i, j, N, shark_size)

            if tmp_distance < distance:
                fish_x = i
                fish_y = j
                distance = tmp_distance
        
        if distance == 1e9: # 갈 수 있는 곳이 없으면
            break

        maps[shark_x][shark_y] = 0
        maps[fish_x][fish_y] = 9

        shark_x = fish_x
        shark_y = fish_y
        
        fish_count += 1
        if fish_count == shark_size:
            shark_size += 1
            fish_count = 0

        move_count += distance

print(move_count)        

