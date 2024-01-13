from collections import deque

# N 세로길이, M 가로길이
N, M = map(int, input().split())

maze = []
for _ in range(N):
    maze.append([int(x) for x in input()])

# 위 아래 왼쪽 오른쪽
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# 방문배열
visited = [[0 for _ in range(M)] for _ in range(N)]


def bfs(x, y, level):
    queue = deque()
    queue.append([y, x, level])

    while queue:
        y, x, level = queue.popleft()

        if y == N - 1 and x == M - 1:
            return level + 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 위치 벗어났을 때
            if nx < 0 or ny < 0 or ny >= N or nx >= M:
                continue

            # 벽일때
            if maze[ny][nx] == 0:
                continue

            # 이미 방문한 곳일 때
            if visited[ny][nx] == 1:
                continue

            queue.append([ny, nx, level + 1])
            visited[ny][nx] = 1

    return -1


print(bfs(0, 0, 0))
