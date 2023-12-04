gears = []
for _ in range(4):
  gears.append(list(map(int, input())))
k = int(input())
actions = []
for _ in range(k):
  actions.append(list(map(int, input().split())))

def rotate(num, direction):
  global gears
  if direction == 1:
    gears[num] = [gears[num][-1]] + gears[num][:-1]
  elif direction == -1:
    gears[num] = gears[num][1:] + [gears[num][0]]

for gear_num, direction in actions:
  temp_gears = gears[:]
  current_direction = direction
  for i in range(gear_num, 4):
    if temp_gears[i-1][2] + temp_gears[i][6] == 1:
      current_direction *= -1
      rotate(i, current_direction)
    else:
      break
  current_direction = direction
  for i in range(gear_num-2, -1, -1):
    if temp_gears[i][2] + temp_gears[i+1][6] == 1:
      current_direction *= -1
      rotate(i, current_direction)
    else:
      break
  rotate(gear_num-1, direction)

print(sum([2 ** i for i in range(4) if gears[i][0] == 1]))