import sys

from typing import *

input = sys.stdin.readline

n, m = 0, 0
# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

board = []


class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __repr__(self):
        return f"({self.y}, {self.x})"


def main():
    global n, m, board, clouds
    n, m = map(int, input().split())

    for _ in range(n):
        row = list(map(int, input().split()))

        board.append(row)

    # 구름 생성
    clouds = []
    clouds.append(Node(n-1, 0))
    clouds.append(Node(n-1, 1))
    clouds.append(Node(n-2, 0))
    clouds.append(Node(n-2, 1))

    for _ in range(m):
        d, s = map(int, input().split())

        for i in range(len(clouds)):
            cloud: Node = clouds[i]

            cloud.y = (cloud.y + dy[d-1]*s) % n
            cloud.x = (cloud.x + dx[d-1]*s) % n

            # 비 내리기
            board[cloud.y][cloud.x] += 1

        # 물 복사 버그 마법
        for cloud in clouds:
            has_water = 0
            for i in range(1, 8, 2):
                ny = cloud.y + dy[i]
                nx = cloud.x + dx[i]

                if is_in(ny, nx) and board[ny][nx] > 0:
                    has_water += 1

            board[cloud.y][cloud.x] += has_water
        not_be_cloud_list = [(cloud.y, cloud.x) for cloud in clouds]

        clouds = []
        # 구름 생성하기
        for i in range(n):
            for j in range(n):
                if can_be_cloud(i, j, not_be_cloud_list) and board[i][j] >= 2:
                    clouds.append(Node(i, j))
                    board[i][j] -= 2

    # 물의 양 합 구하기
    water = 0
    for i in range(n):
        for j in range(n):
            water += board[i][j]

    print(water)


def is_in(y: int, x: int):
    global n
    return y >= 0 and x >= 0 and y < n and x < n


def can_be_cloud(i: int, j: int, not_be_cloud_list: list):
    for y, x in not_be_cloud_list:
        if i == y and j == x:
            return False
    return True


if __name__ == "__main__":
    main()
