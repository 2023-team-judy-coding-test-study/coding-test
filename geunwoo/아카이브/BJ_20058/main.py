import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

n, q = 0, 0
board = []
visited = []

dy = [0,0,-1,1]
dx = [-1,1,0,0]

max_ice = 0


class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x


def turn_board(l: int):
    global board, n, q, dy, dx, visited, max_ice

    new_board = [[0 for _ in range(2**n)] for _ in range(2**n)]

    for i in range(0, 2 ** n, 2 ** l):
        for j in range(0, 2 ** n, 2 ** l):
            for k in range(2 ** l):
                for m in range(2 ** l):
                    new_board[i+k][j+m] = board[i+(2**l-m-1)][j+k]

    board = deepcopy(new_board)


def melt_ice():
    global board, n, q, dy, dx, visited, max_ice

    new_board = [[0 for _ in range(2 ** n)] for _ in range(2 ** n)]

    for y in range(2**n):
        for x in range(2**n):

            cnt = 0
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if ny < 0 or nx < 0 or ny >= 2**n or nx >= 2**n:
                    continue

                if board[ny][nx] > 0:
                    cnt += 1

            if cnt < 3:
                new_board[y][x] = board[y][x] - 1 if board[y][x] > 0 else 0
            else:
                new_board[y][x] = board[y][x]

    board = deepcopy(new_board)


def count_ice():
    global board, n, q, dy, dx, visited, max_ice

    sum = 0

    for y in range(2 ** n):
        for x in range(2 ** n):

            sum += board[y][x]

    return sum


def set_max_size_ice():
    global board, n, q, dy, dx, visited, max_ice

    visited = [[0 for _ in range(2**n)] for _ in range(2**n)]
    for y in range(2 ** n):
        for x in range(2 ** n):
            if board[y][x] > 0 and visited[y][x] == 0:
                bfs(Node(y, x))


def bfs(node: Node):
    global board, n, q, dy, dx, visited, max_ice

    if board[node.y][node.x] <= 0:
        return

    if visited[node.y][node.x]:
        return

    q = deque()
    q.append(node)
    visited[node.y][node.x] = 1
    size_cnt = 1

    while q:
        now = q.popleft()

        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]

            if ny < 0 or nx < 0 or ny >= 2 ** n or nx >= 2 ** n:
                continue

            if board[ny][nx] <= 0:
                continue

            if visited[ny][nx] == 1:
                continue

            q.append(Node(ny, nx))
            visited[ny][nx] = 1
            size_cnt += 1

    max_ice = max(max_ice, size_cnt)

    return


def main():
    global board, n, q, max_ice
    n, q = map(int, input().strip().split())
    board = []

    # 1. init
    for i in range(2**n):
        row = list(map(int, input().strip().split()))
        board.append(row)

    l_list = list(map(int, input().strip().split()))

    for l in l_list:
        # 2. 부분 격자를 시계방향으로 이동
        turn_board(l)

        # 3. 얼음 녹이기
        melt_ice()

    # 4. 얼음 총 갯수 구하기
    total = count_ice()

    # 5. 가장 큰 얼음 크기 구하기 (BFS)
    set_max_size_ice()

    # 정답 출력
    print(total)
    print(max_ice)


if __name__ == '__main__':
    main()