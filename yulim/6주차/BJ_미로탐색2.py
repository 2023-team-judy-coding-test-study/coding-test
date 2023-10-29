from collections import deque

N, M = map(int, input().split())

maze = []

for _ in range(N):
    maze.append([int(x) for x in input()])

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[0 for _ in range(M)] for _ in range(N)]


def bfs(x, y, level):
    queue = deque()
    queue.append([x, y, level])  # ??

    while queue:
        x, y, level = queue.popleft()

        if x == M - 1 and y == N - 1:
            return level + 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue

            if visited[ny][nx] == 1:
                continue

            if maze[ny][nx] == 0:
                continue

            queue.append([nx, ny, level + 1])
            visited[ny][nx] = 1
    return 0


print(bfs(0, 0, 0))
