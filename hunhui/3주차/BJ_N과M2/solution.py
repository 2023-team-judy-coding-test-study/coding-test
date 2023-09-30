n,m=list(map(int, input().split()))
answer, is_visited = [], [False]*n

def backtracking(depth, start):
  # 탈출 조건: m개의 숫자를 찾으면 종료
  if depth == m:
    print(' '.join(answer))
    return
  # 가지 치기: 방문한 곳이 아니면 방문하고 다시 재귀호출
  # start 변수를 추가하여 자기보다 높은 숫자만 탐색하도록함
  for i in range(start, n):
    if not is_visited[i]:
      is_visited[i] = True
      answer.append(str(i+1))
      backtracking(depth+1, i+1)
      answer.pop()
      is_visited[i] = False

backtracking(0,0)