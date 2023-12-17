# 20:20
from collections import Counter
y, x, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(3)]

def new_sort(values):
  val_counter = Counter([val for val in values if val != 0])
  new_values = [(key, value) for key, value in val_counter.items()]
  new_values.sort(key=lambda val: (val[1], val[0]))
  answer = []
  for key, value in new_values:
    answer.append(key)
    answer.append(value)
  return answer

def row_sort():
  y_len = len(grid)
  new_values = [new_sort(row) for row in grid]
  max_len = min(max([len(val) for val in new_values]), 100)
  answer = [[0]*max_len for _ in range(y_len)]
  for y in range(y_len):
    for x, val in enumerate(new_values[y]):
      if x >= max_len:
        break
      answer[y][x] = val
  return answer 

def col_sort():
  x_len, y_len = len(grid[0]), len(grid)
  new_values = [new_sort([grid[y][x] for y in range(y_len)]) for x in range(x_len)]
  max_len = min(max([len(val) for val in new_values]), 100)
  answer = [[0]*x_len for _ in range(max_len)]
  for x in range(x_len):
    for y, val in enumerate(new_values[x]):
      if y >= max_len:
        break
      answer[y][x] = val
  return answer

max_time = 0
while True:
  if len(grid) > y-1 and len(grid[0]) > x-1 and grid[y-1][x-1] == k:
    break
  if max_time == 100:
    max_time = -1
    break
  col_count, row_count = len(grid[0]), len(grid)
  max_time += 1
  if row_count >= col_count:
    grid = row_sort()
  else:
    grid = col_sort()

print(max_time)