import sys

from collections import deque

imput = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


n, m = 0, 0
r, c, d = 0, 0, 0

board = []
visited = []


class Node:
    def __init__(self, y, x, d, level):
        self.y = y
        self.x = x
        self.d = d
        self.level = level

    def __repr__(self):
        return f"({self.y}, {self.x}, {self.d}, {self.level})"


def main():
    global n, m, r, c, d, board, visited

    n, m = map(int, input().split())
    r, c, d = map(int, input().split())

    for _ in range(n):
        row = list(map(int, input().split()))

        board.append(row)

    now = Node(r, c, d, 0)
    answer = bfs(now)
    print(answer)


def bfs(node: Node):
    global n, m, r, c, d, board

    now = node
    cnt = 0
    while True:
        if board[now.y][now.x] == 0:
            board[now.y][now.x] = 2
            cnt += 1
            now = Node(now.y, now.x, now.d, now.level + 1)

        not_cleaned = 0
        # 4방향으로 이동 조건 확인
        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue

            # 청소되지 않은 구역을 발견한 경우
            if board[ny][nx] == 0:
                not_cleaned += 1
                break

        if not_cleaned:
            direction = (now.d - 1) % 4

            ny = now.y + dy[direction]
            nx = now.x + dx[direction]

            # 청소되지 않은 구역을 발견한 경우
            if board[ny][nx] == 0:
                now = Node(ny, nx, direction, now.level+1)
            else:
                now = Node(now.y, now.x, direction, now.level)

        else:
            direction = (now.d + 2) % 4

            ny = now.y + dy[direction]
            nx = now.x + dx[direction]

            # 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춤
            if board[ny][nx] == 1:
                return cnt
            # 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진
            else:
                now = Node(ny, nx, now.d, now.level)


if __name__ == "__main__":
    main()
