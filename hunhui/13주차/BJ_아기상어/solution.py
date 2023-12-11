# 22:48
from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

#상어위치
shark_x, shark_y = None, None
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            shark_x, shark_y = i, j
            graph[i][j] = 0
            break

dirs = [(0,1), (0,-1), (1,0), (-1,0)]

def biteFish(x,y,shark_size):
  distance = [[0] * n for _ in range(n)]
  visited = [[False] * n for _ in range(n)]
  # 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값이다. (bfs사용)
  q = deque([(x,y)])
  visited[x][y] = 1
  temp = []
  while q:
    cur_x, cur_y = q.popleft()
    for dx, dy in dirs:
      nx, ny = cur_x + dx, cur_y + dy
      if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] <= shark_size:
        q.append((nx,ny))
        visited[nx][ny] = 1
        distance[nx][ny] = distance[cur_x][cur_y] + 1
        if graph[nx][ny] < shark_size and graph[nx][ny] != 0:
          temp.append((nx,ny,distance[nx][ny]))
  # 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹는다.
  return sorted(temp, key=lambda x: (-x[2],-x[0],-x[1]))

size, exp = 2, 0
result = 0
while True:
    shark = biteFish(shark_x, shark_y, size)
    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청한다.
    if len(shark) == 0:
        break
    nx, ny, dist = shark.pop()
    shark_x, shark_y = nx, ny
    graph[shark_x][shark_y] = 0
    result += dist
    exp += 1
    if exp == size:
      size += 1; exp = 0
print(result)