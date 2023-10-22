from collections import deque

n: int
m: int

board = []
visited = []

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


class Node:
    def __init__(self, y, x, level):
        self.y = y
        self.x = x
        self.level = level


def bfs(node: Node):
    global n, m, board, visited, dy, dx

    q = deque()

    q.append(node)
    visited[node.y][node.x] = 1

    while q:
        now = q.popleft()

        if now.y == n-1 and now.x == m-1:
            return now.level

        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue

            if board[ny][nx] == 0:
                continue

            if visited[ny][nx] == 1:
                continue

            q.append(Node(ny, nx, now.level + 1))
            visited[ny][nx] = 1

        # 종료시점

    return -1


def main():
    """
    미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다.
    이러한 미로가 주어졌을 때, 
    (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램

    4 6
    101111
    101010
    101011
    111011
    """
    global n, m, board, visited, dy, dx

    n, m = map(int, input().split())

    board = []
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(n):
        row = list(map(int, list(input())))

        board.append(row)

    ans = bfs(Node(0, 0, 1))

    print(ans)


if __name__ == "__main__":
    main()
