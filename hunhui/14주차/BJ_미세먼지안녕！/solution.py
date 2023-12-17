# 19:02
import copy
r, c, t = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(r)]

air_cleaner_pos = []
for i in range(r):
  if room[i][0] == -1:
    air_cleaner_pos.append((0,i))
    air_cleaner_pos.append((0,i+1))
    break

dirs = [(1,0),(-1,0),(0,1),(0,-1)]
def dust_move():
  temp = copy.deepcopy(room)
  for y in range(r):
    for x in range(c):
      amount = room[y][x]
      if amount <= 0:
        continue
      move_amount = amount // 5
      if move_amount == 0:
        continue
      count = 0
      for dx, dy in dirs:
        nx, ny = dx + x, dy + y
        if nx >= 0 and nx < c and ny >= 0 and ny < r and (nx, ny) not in air_cleaner_pos:
          temp[ny][nx] += move_amount
          count += 1
      temp[y][x] -= move_amount * count
  return temp

def active_air_cleaner():
  x1, y1 = air_cleaner_pos[0]
  x2, y2 = air_cleaner_pos[1]
  for y in range(y1-2, -1, -1):
    room[y+1][x1] = room[y][x1]
  for x in range(1, c):
    room[0][x-1] = room[0][x]
  for y in range(1, y1+1):
    room[y-1][c-1] = room[y][c-1]
  for x in range(c-1, x1+1, -1):
    room[y1][x] = room[y1][x-1]
  room[y1][x1+1] = 0

  for y in range(y2+2, r):
    room[y-1][x2] = room[y][x2]
  for x in range(1, c):
    room[r-1][x-1] = room[r-1][x]
  for y in range(r-2, y2-1, -1):
    room[y+1][c-1] = room[y][c-1]
  for x in range(c-1, x2+1, -1):
    room[y2][x] = room[y2][x-1]
  room[y2][x2+1] = 0

for _ in range(t):
  room = dust_move()
  active_air_cleaner()

print(sum(sum(r) for r in room)+2)