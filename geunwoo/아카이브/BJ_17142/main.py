import sys
from collections import deque
from typing import List

INF = sys.maxsize
input = sys.stdin.readline

dy = [0,0,-1,1]
dx = [-1,1,0,0]

n, m = 0, 0

board = []
visited = []
virus_list = []

min_cost = INF

class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __repr__(self):
        return f"({self.y}, {self.x})"


def select_and_spread(idx: int, q: deque):
    global n, m, board, visited, virus_list, min_cost
    # 종료 조건
    if len(q) == m:
        selected = list(q)
        cost = spread(selected)

        min_cost = min(min_cost, cost)
        return

    if idx == len(virus_list):
        return

    # 가지 치기
    q.append(virus_list[idx])
    select_and_spread(idx + 1, q)

    q.pop()
    select_and_spread(idx + 1, q)


def spread(selected: List[Node]):
    global n, m, board, visited, virus_list
    visited = [[-1 for _ in range(n)] for _ in range(n)]
    q = deque()

    for virus in selected:
        q.append(virus)
        visited[virus.y][virus.x] = 0

    while q:
        now: Node = q.popleft()

        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue

            if board[ny][nx] == 1:
                continue

            if visited[ny][nx] != -1:
                continue

            visited[ny][nx] = visited[now.y][now.x] + 1
            q.append(Node(ny, nx))

    level = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                if visited[i][j] == -1:
                    return INF

                level = max(level, visited[i][j])

    return level


def main():
    """
    확산
    1초에 상하좌우 한칸씩 퍼짐
    활성이 비활성을 만나면 비활성 -> 활성

    1. 바이러스 선택
    2. 확산
    3. 시간 비교
    """
    global n, m, board, visited, virus_list, min_cost

    n, m = map(int, input().split())

    board = [[0 for _ in range(n)] for _ in range(n)]
    virus_list = []

    for i in range(n):
        row = list(map(int, input().split()))

        for j in range(n):
            board[i][j] = row[j]

            if board[i][j] == 2:
                virus_list.append(Node(i, j))

    select_and_spread(0, deque())

    if min_cost == INF:
        print(-1)
    else:
        print(min_cost)


if __name__ == '__main__':
    main()