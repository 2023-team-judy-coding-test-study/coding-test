from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
lab = []
for _ in range(n):
  lab.append(list(map(int, input().split())))

virus_pos = []
empty_count = 0
max_safe_count = 0

for y in range(n):
  for x in range(m):
    if lab[y][x] == 2:
      virus_pos.append((x,y))
    if lab[y][x] == 0:
      empty_count += 1

dirs = [(1,0),(-1,0),(0,1),(0,-1)]

# 벽 3개 만들기
# 바이러스 퍼트리기(bfs)
# 안전 영역 크기 재기 -> n * m - (벽의 수 + 바이러스 퍼진 곳 수)
# 반복

def make_wall(count):
  global max_safe_count
  if count == 3:
    max_safe_count = max(bfs(), max_safe_count)
    return
  
  for y in range(n):
    for x in range(m):
      if lab[y][x] == 0:
        lab[y][x] = 1
        make_wall(count+1)
        lab[y][x] = 0

def bfs():
  temp_lab = deepcopy(lab)
  que = deque(virus_pos)
  count = 0
  while que:
    x, y = que.pop()
    for dx, dy in dirs:
      nx, ny = x + dx, y + dy
      if nx >= 0 and nx < m and ny >= 0 and ny < n and temp_lab[ny][nx] == 0:
        count += 1
        que.append((nx, ny))
        temp_lab[ny][nx] = 2
  return empty_count - count

make_wall(0)

print(max_safe_count - 3)