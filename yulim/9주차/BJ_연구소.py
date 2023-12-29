from collections import deque
import copy

N, M = map(int, input().split())

maps = [[int(x) for x in input().split()] for _ in range(N)]
maps = []

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    tmp_maps = copy.deepcopy(maps)
    queue = deque()
    
    for i in range(N):
        for j in range(M):
            if tmp_maps[i][j] == 2:
                queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if  0 > nx or N <= nx or 0 > ny or M <= ny:
                continue
            
            elif tmp_maps[nx][ny] == 0:
                tmp_maps[nx][ny] = 2
                queue.append((nx, ny))

    global answer
    cnt = 0
    for i in range(N):
        cnt += tmp_maps[i].count(0)
    answer = max(answer, cnt)


def makeWall(cnt):
    if cnt == 3: 
        bfs()
        return
    
    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                maps[i][j] = 1
                makeWall(cnt + 1)
                maps[i][j] = 0 

# for i in range(N):
#     maps.append(list(map(int, input().split())))

answer = 0
makeWall(0)
print(answer)