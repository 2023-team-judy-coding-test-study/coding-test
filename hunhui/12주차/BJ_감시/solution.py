# 16:27
import math, copy

n,m = map(int, input().split())
grid = []
for _ in range(n):
  grid.append(list(map(int, input().split())))

# 방향 정보(동 남 서 북)
dirs = [(1,0),(0,1),(-1,0),(0,-1)]

# CCTV 감시 방향 정보(동 남 서 북)
cctv_infos = [
  None,
  [(1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1)],
  [(1,0,1,0),(0,1,0,1)],
  [(1,1,0,0),(0,1,1,0),(0,0,1,1),(1,0,0,1)],
  [(0,1,1,1),(1,0,1,1),(1,1,0,1),(1,1,1,0)],
  [(1,1,1,1)]
]

count = 0
cctvs = []
for y in range(n):
  for x in range(m):
    num = grid[y][x]
    if num == 0:
      count += 1
    elif num != 6:
       cctvs.append((num, x, y))

answer = math.inf

# current_grid는 탐색이 된 곳 표시, count는 사각지대 수, depth는 탐색한 cctv수
def backtracking(current_grid,count,depth):
  global answer
  if depth == len(cctvs):
    answer = min(answer, count)
    return
  
  cctv_num, cx, cy = cctvs[depth]
  for cctv_dirs in cctv_infos[cctv_num]:
    temp_grid = copy.deepcopy(current_grid)
    temp_count = count
    for i, num in enumerate(cctv_dirs):
      if num == 0:
        continue
      dx, dy = dirs[i]
      nx, ny = cx, cy
      temp_grid[ny][nx] = 7
      while nx >= 0 and nx < m and ny >= 0 and ny < n and temp_grid[ny][nx] != 6:
        if temp_grid[ny][nx] == 0:
          temp_grid[ny][nx] = 7
          temp_count -= 1
        nx += dx
        ny += dy
    backtracking(copy.deepcopy(temp_grid),temp_count,depth+1)

backtracking(grid,count,0)

print(answer)