import sys

from collections import deque

input = sys.stdin.readline

n = 0
board = []
visited = []

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x


def main():
    global n, board, visited
    """
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
    """

    n = int(input())

    for _ in range(n):
        row = list(map(int, list(input().strip())))

        board.append(row)

    visited = [[0 for _ in range(n)] for _ in range(n)]

    towns = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                continue

            if visited[i][j] == 1:
                continue

            towns.append(bfs(Node(i, j)))

    towns.sort()
    print(len(towns))
    for t in towns:
        print(t)


def bfs(node: Node):
    global n, board, visited
    cnt = 0

    q = deque()

    q.append(node)
    visited[node.y][node.x] = 1
    cnt += 1

    while q:
        now = q.popleft()

        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue

            if board[ny][nx] == 0:
                continue

            if visited[ny][nx] == 1:
                continue

            q.append(Node(ny, nx))
            visited[ny][nx] = 1
            cnt += 1

    return cnt


if __name__ == "__main__":
    main()
