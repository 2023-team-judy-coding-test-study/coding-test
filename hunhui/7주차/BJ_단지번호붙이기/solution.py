n = int(input())

homeMap = []
for _ in range(n):
  homeMap.append(list(map(int, input())))

dirs = [(1,0),(-1,0),(0,1),(0,-1)]
isVisited = [[h == 0 for h in line] for line in homeMap]
counts = []
tempCount = 0

def dfs(x,y):
  global tempCount
  isVisited[y][x] = True
  tempCount += 1
  for dx, dy in dirs:
    nx, ny = x + dx, y + dy
    if nx >= 0 and nx < n and ny >= 0 and ny < n and not isVisited[ny][nx]:
      dfs(nx,ny)

for y in range(n):
  for x in range(n):
    if not isVisited[y][x]:
      dfs(x,y)
      counts.append(tempCount)
      tempCount = 0

print(len(counts))
counts.sort()
[print(count) for count in counts]