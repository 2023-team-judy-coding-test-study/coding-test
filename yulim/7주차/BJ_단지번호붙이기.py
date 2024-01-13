from collections import deque

n = int(input())
maps = [[int(x) for x in input()] for _ in range(n)]

# 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    maps[x][y] = 0
    count = 1

    while queue:
        tmp_x, tmp_y = queue.popleft()
        for i in range(4):
            nx = tmp_x + dx[i]
            ny = tmp_y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = 0
                queue.append((nx, ny))
                count += 1
    return count

cnt = []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            cnt.append(bfs(i, j))

cnt.sort()
print(len(cnt))
for c in cnt:
    print(c)

              