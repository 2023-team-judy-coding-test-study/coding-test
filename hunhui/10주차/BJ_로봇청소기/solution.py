# 00: 01:43
n, m = map(int, input().split())
y, x, current_dir = list(map(int, input().split()))
game_map = []
for _ in range(n):
  game_map.append(list(map(int, input().split())))

# 북 동 남 서
dirs = [(0,-1),(1,0),(0,1),(-1,0)]

count = 0
while True:
  if x < 0 or x >= m or y < 0 or y >= n or game_map[y][x] == 1:
    break
  # 1. 청소되지 않은 경우 청소
  if game_map[y][x] == 0:
    game_map[y][x] = 2
    count += 1
  can_clean = False
  # 2. 90도씩 회전하며 확인하며 앞 방향에 청소되지 않은 경우 전진하고 반복
  for _ in range(4):
    # 회전
    current_dir = (current_dir - 1) % 4
    dx, dy = dirs[current_dir]
    nx, ny = x + dx, y + dy
    # 벽이 아니고, 청소되지 않았으면 이동
    if nx >= 0 and nx < m and ny >= 0 and ny < n and game_map[ny][nx] == 0:
      x += dx
      y += dy
      can_clean = True
      break
  # 3. 청소할 곳이 없으면 후진한뒤 반복
  if not can_clean:
    dx, dy = dirs[current_dir]
    x -= dx
    y -= dy

print(count)