import sys
import copy
from collections import deque
from typing import List

input = sys.stdin.readline

WALL = 1
VIRUS = 2

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]
board = []
n = 0
m = 0
max_safe_area = 0


class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x


def bfs(node: Node):
    global n, m, board

    q = deque()
    q.append(node)

    while q:
        now: Node = q.popleft()

        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= m:
                continue

            if board[ny][nx] > 0:
                continue

            board[ny][nx] = VIRUS
            q.append(Node(ny, nx))


def select_wall(count: int, virus_list: List[Node]):
    global n, m, board, max_safe_area
    # 종료 조건
    if count >= 3:
        temp_board = copy.deepcopy(board)

        # 바이러스 퍼트리기
        for virus in virus_list:
            bfs(virus)

        # 안전 영역 계산
        safe_area = 0
        for i in range(n):
            for j in range(m):
                if board[i][j] == 0:
                    safe_area += 1

        # 최대 안전 영역 비교
        if safe_area > max_safe_area:
            max_safe_area = safe_area

        board = temp_board
        return

    # 가지 치기
    for i in range(n):
        for j in range(m):
            if board[i][j] != 0:
                continue
            board[i][j] = 1
            select_wall(count + 1, virus_list)
            board[i][j] = 0


def main():
    global n, m, board, max_safe_area
    # 연구소 초기화
    n, m = map(int, input().split())

    virus_list = []
    for i in range(n):
        row = list(map(int, input().split()))

        for j in range(m):
            if row[j] == VIRUS:
                virus_list.append(Node(i, j))

        board.append(row)

    # 3개의 벽 선택
    select_wall(0, virus_list)

    print(max_safe_area)


if __name__ == '__main__':
    main()
