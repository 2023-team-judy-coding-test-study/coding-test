n,m=list(map(int, input().split()))
nums=sorted(list(map(int, input().split())))
answer = []
is_visited = [False]*n

def backtracking(depth):
  # 탈출 조건: m개의 숫자를 찾으면 종료
  if depth == m:
    print(' '.join(answer))
    return
  # 가지 치기: 탐색한 답 추가 후 재귀호출
  for i in range(n):
    if not is_visited[i]:
      is_visited[i] = True
      answer.append(str(nums[i]))
      backtracking(depth+1)
      answer.pop()
      is_visited[i] = False

backtracking(0)