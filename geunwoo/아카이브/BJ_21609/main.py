import sys
from collections import deque
from typing import List

input = sys.stdin.readline

n, m = 0, 0

board = []
visited = []

dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]


class Node:
    def __init__(self, y, x, color):
        self.y = y
        self.x = x
        self.color = color

    def __repr__(self):
        return f"({self.y}, {self.x}, {self.color})"


def has_block_group():
    global n, m, board, visited

    visited = [[0 for _ in range(n)] for _ in range(n)]

    for y in range(n):
        for x in range(n):
            if board[y][x] > 0 and visited[y][x] == 0:
                block_group: List[Node] = _bfs(Node(y, x, board[y][x]))

                if block_group:
                    return True

    return False


def find_max_block_group() -> List[Node]:
    global n, m, board, visited

    visited = [[0 for _ in range(n)] for _ in range(n)]
    block_group_list: List[List[Node]] = []

    max_group_len = 0
    block_group_list_len = 0

    for y in range(n):
        for x in range(n):
            # print(f"start find with y: {y}, x: {x}, color: {board[y][x]}, visited: {visited[y][x]}")
            if board[y][x] > 0 and visited[y][x] == 0:
                block_group: List[Node] = _bfs(Node(y, x, board[y][x]))

                if block_group:
                    block_group_list.append(block_group)

                    block_group_list_len += 1
                    max_group_len = max(max_group_len, len(block_group))

    if block_group_list_len == 1:
        return block_group_list[0]

    rainbow_cnt_list = []
    max_rainbow_cnt = 0

    new_block_group_list = []
    block_group_list_len = 0
    for block_group in block_group_list:
        if len(block_group) == max_group_len:
            new_block_group_list.append(block_group)
            block_group_list_len += 1

            # 무지개 블록 개수 저장
            rainbow_cnt = 0
            for block in block_group:
                if block.color == 0:
                    rainbow_cnt += 1
            rainbow_cnt_list.append(rainbow_cnt)
            max_rainbow_cnt = max(max_rainbow_cnt, rainbow_cnt)

    block_group_list = new_block_group_list

    if block_group_list_len == 1:
        return block_group_list[0]

    new_block_group_list = []
    block_group_list_len = 0
    for idx, rainbow_cnt in enumerate(rainbow_cnt_list):
        if rainbow_cnt == max_rainbow_cnt:
            new_block_group_list.append(block_group_list[idx])
            block_group_list_len += 1
    block_group_list = new_block_group_list

    if block_group_list_len == 1:
        return block_group_list[0]

    block_group_list = sorted(block_group_list, key=lambda block_list: (-block_list[0].y, -block_list[0].x))

    return block_group_list[0]


def remove_block_group(block_group: List[Node]) -> int:
    """블록 그룹을 제거하고 블럭 갯수^2 만큼 점수를 획득"""
    global n, m, board, visited

    block_cnt = 0

    for block in block_group:
        board[block.y][block.x] = -2

        block_cnt += 1

    return block_cnt ** 2


def effect_by_gravity():
    """버블소트를 이용한 중력 작용 구현
    가장 큰 행에서부터 0행까지 버블소트
    - 검은 블록 (-1)을 만나면 소트하지 않음.
    - 비어있는 칸을 0행으로 순차적으로 이동.
    """
    global n, m, board, visited

    for j in range(n):
        for i in range(n-1, 0, -1):
            for k in range(n-1, 0, -1):
                if board[k][j] == -1 or board[k-1][j] == -1:
                    continue

                if board[k][j] >= 0:
                    continue

                board[k][j], board[k-1][j] = board[k-1][j], board[k][j]


def turn_r_clock():
    """2차원 배열을 반시계 방향으로 회전"""
    global n, m, board, visited

    for _ in range(3):
        _turn_clock()


def _turn_clock():
    """2차원 배열 시계 방향으로 회전"""
    global n, m, board, visited

    new_board = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new_board[i][j] = board[n - 1 - j][i]

    board = new_board


def _bfs(node: Node) -> List[Node]:
    global n, m, board, visited

    standard_color = node.color

    q = deque()
    q.append(node)
    visited[node.y][node.x] = 1

    block_group: List[Node] = [node]  # 첫번째 인덱스의 블록이 기준 블록

    while q:
        now: Node = q.popleft()

        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if board[ny][nx] != 0 and board[ny][nx] != standard_color:
                continue
            if visited[ny][nx] > 0:
                continue

            next_node: Node = Node(ny, nx, board[ny][nx])
            visited[ny][nx] = 2 if board[ny][nx] == 0 else 1  # 무지개 블록과 일반 블록의 방문 기록 구분

            q.append(next_node)
            block_group.append(next_node)

    # 무지개 블록 방문 기록 제거
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 2:
                visited[i][j] = 0

    # 블록 그룹 크기 < 2이면 그룹 x
    if len(block_group) < 2:
        return []

    return block_group


def main():
    global n, m, board, visited
    """
    블록 : 검은색, 무지개, 일반
    - 일반 : M가지 색상, M이하의 자연수
    - 검은색 : -1
    - 무지개 : 0

    블록 그룹
    - 일반 블록이 적어도 하나 존재
    - 일반 블록의 색은 모두 같아야 함
    - 검은색 블록은 포함되면 안됨
    - 무지개 블록은 얼마나 있든 상관 없음
    - 그룹에 속한 블록 개수 >= 2
    - 기준 블록 : 블록 중 행, 열의 번호가 가장 작은 블록 (무지개 x)

    오토 플레이 기능
    - 블록 그룹 존재시 계속 반복

    1. 크기가 가장 큰 블록 그룹 찾기
    - 무지개 블록의 수가 가장 많은 그룹, 기준 블록의 행이 가장 큰 것, 기준 블록의 열이 가장 큰 것

    2. 1에서 찾은 블록 그룹의 모든 블록 제거
    - 블록 수 ^ 2 점 획득

    3. 격자 중력 작용
    - 검은색 블록 제외 모든 블록의 행의 번호가 큰 칸으로 이동

    4. 격자 90도 반시계 방향 회전

    5. 다시 격자에 중력 작용
    """

    # init
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    score = 0
    while has_block_group():

        # 1. 크기가 가장 큰 블록 그룹 찾기
        max_block_group: List[Node] = find_max_block_group()

        # 2. 1에서 찾은 블록 그룹의 모든 블록 제거
        score += remove_block_group(max_block_group)

        # 3. 격자 중력 작용
        effect_by_gravity()

        # 4. 격자 90도 반시계 방향 회전
        turn_r_clock()

        # 5. 격자 중력 작용
        effect_by_gravity()

    print(score)


if __name__ == "__main__":
    main()
