import sys

from collections import deque

input = sys.stdin.readline

SHARK = 9

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
n = 0

board = []


class Node:
    def __init__(self, y, x, size, sec, eat_count):
        self.y = y
        self.x = x
        self.size = size
        self.sec = sec
        self.eat_count = eat_count

    def __str__(self):
        return f"y: {self.y}, x: {self.x}, size: {self.size}, sec: {self.sec}, eat_count: {self.eat_count}"


def bfs(node: Node):
    global n, board
    visited = [[0 for _ in range(n)] for _ in range(n)]

    visited[node.y][node.x] = 1

    q = deque()
    q.append(node)

    fish_list = []
    fix_sec = int(1e9)
    while q:
        now: Node = q.popleft()

        # 종료 조건
        if len(fish_list) > 0 and now.sec > fix_sec:
            # y 기준 내림차 순(위쪽), x 기준 오름차 순(왼쪽)
            fish_list.sort(key=lambda fish: (fish[0], fish[1]))

            ny = fish_list[0][0]
            nx = fish_list[0][1]

            board[node.y][node.x] = 0
            board[ny][nx] = SHARK
            new_node = Node(ny, nx, node.size, now.sec, node.eat_count + 1)
            if new_node.size == new_node.eat_count:
                new_node.size += 1
                new_node.eat_count = 0
            return new_node

        # 가지 치기
        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue

            if visited[ny][nx] == 1:
                continue

            if board[ny][nx] > 0:
                if now.size < board[ny][nx]:
                    continue

                if now.size > board[ny][nx]:
                    fix_sec = now.sec
                    fish_list.append([ny, nx])

            visited[ny][nx] = 1
            q.append(Node(ny, nx, now.size, now.sec + 1, now.eat_count))

    return node


def main():
    global n, board
    # init board
    n = int(input())

    shark_pos = Node(0, 0, 2, 0, 0)
    for i in range(n):
        row = list(map(int, input().split()))
        board.append(row)

        # find shark position
        for j in range(n):
            if row[j] == SHARK:
                shark_pos = Node(i, j, 2, 0, 0)

    while True:
        now: Node = shark_pos
        shark_next_pos: Node = bfs(node=now)

        if shark_next_pos.eat_count == now.eat_count:
            shark_pos = now
            break

        shark_pos = shark_next_pos

    print(shark_pos.sec)


if __name__ == '__main__':
    main()
