n, m = map(int, input().split())
visited = [0]*(n+1)
answer = []

def backtracking(level):
  global visited, n, m

  if level == m:
    print(' '.join(answer))
    return
  
  for i in range(1,n+1):
    if visited[i] == 0:
      visited[i] = 1
      answer.append(str(i))
      backtracking(level+1)
      visited[i] = 0
      answer.pop()

backtracking(0)