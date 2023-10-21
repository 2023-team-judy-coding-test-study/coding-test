from collections import deque

n,m=list(map(int, input().split()))
maze = [[int(i) for i in str(input())] for _ in range(n)]
dirs = [(1,0),(-1,0),(0,1),(0,-1)]

def isIn(x,y):
  return x < m and y < n and x >= 0 and y >= 0

def bfs(x,y):
  posQue = deque()
  posQue.append((x,y))
  while posQue:
    x, y = posQue.popleft()
    for dx, dy in dirs:
      newX, newY = x + dx, y + dy
      if isIn(newX, newY) and maze[newY][newX] == 1:
        posQue.append((newX,newY))
        maze[newY][newX] = maze[y][x] + 1
  return maze[n-1][m-1]
    
print(bfs(0,0))