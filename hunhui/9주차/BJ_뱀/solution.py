# 00: 48
from collections import deque

# 시계 방향 (우 -> 하 -> 좌 -> 상)
dirs = [(1,0),(0,1),(-1,0),(0,-1)]

n = int(input())
game_map = [[0]*n for _ in range(n)]

k = int(input())
for _ in range(k):
  y, x = list(map(int, input().split()))
  # 사과가 위치한 곳의 값을 1로 설정
  game_map[y-1][x-1] = 1

move_plan = []
l = int(input())
for _ in range(l):
  info = input().split()
  move_plan.append((int(info[0]), 1 if info[1] == 'D' else -1)) # (sec, dir_value)

current_dir = 0 # 오른쪽으로 돌리면 (current_dir+1)%4, 왼쪽으로 돌리면 (current_dir-1)%4
current_sec = 0
x, y = 0, 0
game_map[0][0] = 2 # 뱀이 있는 곳의 값을 2로 설정
tail_que = deque()
tail_que.append((0,0))
is_move_stop = False
for sec, dir_value in move_plan:
  dx, dy = dirs[current_dir]
  # 다음 방향 전환 까지 이동
  for _ in range(sec - current_sec):
    current_sec += 1
    x += dx
    y += dy
    if x < 0 or x >= n or y < 0 or y >= n or game_map[y][x] == 2:
      is_move_stop = True
      break
    if game_map[y][x] == 0:
      tx, ty = tail_que.popleft()
      game_map[ty][tx] = 0
    tail_que.append((x,y))
    game_map[y][x] = 2

  if is_move_stop:
    break
  current_dir = (current_dir + dir_value) % 4

if not is_move_stop:
  dx, dy = dirs[current_dir]
  while True:
    current_sec += 1
    x += dx
    y += dy
    if x < 0 or x >= n or y < 0 or y >= n or game_map[y][x] == 2:
      break
    if game_map[y][x] == 0:
      tx, ty = tail_que.popleft()
      game_map[ty][tx] = 0
    tail_que.append((x,y))
    game_map[y][x] = 2

print(current_sec)