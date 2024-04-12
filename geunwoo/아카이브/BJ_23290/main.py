import sys
from typing import List
from copy import copy, deepcopy

input = sys.stdin.readline

#  ←, ↖, ↑, ↗, →, ↘, ↓, ↙
fdy = [0, -1, -1, -1, 0, 1, 1, 1]
fdx = [-1, -1, 0, 1, 1, 1, 0, -1]

fd_map = {
    0: '←',
    1: '↖',
    2: '↑',
    3: '↗',
    4: '→',
    5: '↘',
    6: '↓',
    7: '↙'
}
#  ↑, ←, ↓, →
sdy = [-1, 0, 1, 0]
sdx = [0, -1, 0, 1]


class Node:
    def __init__(self, y, x, d, status, cnt):
        self.y = y
        self.x = x
        self.d = d
        self.status = status  # 0: shark, 1: fish, 2: death
        self.cnt = cnt

    def __repr__(self):
        s = "?"
        if self.status == 0:
            s = "상"
        elif self.status == 1:
            s = "물"
        elif self.status == 2:
            s = "냄"

        return f"({s})"


m = 0
s = 0
n = 4
fish_list = []
shark = [0, 0, 0, 0, 0]
shark_route_list = []

board: List[List[List[List[int]]]] = [[[] for _ in range(n)] for _ in range(n)]


def init():
    global m, s, n, fish_list, shark, shark_route_list, board
    # 물고기 수, 연습 횟수
    m, s = map(int, input().split())

    fish_list = []
    # 물고기 목록 초기화
    for _ in range(m):
        y, x, d = map(int, input().split())

        fish_list.append([y - 1, x - 1, d - 1, 1, 0])

    # 상어 초기화
    y, x = map(int, input().split())
    shark = [y - 1, x - 1, 0, 0, 0]
    _set_shark_route_list(0, "", 3)

    # 격자 초기화
    _set_board()


def count_fish_smell():
    for fish in fish_list:
        if fish[2] == 2:
            fish[4] += 1


def copy_fish():
    fishes = []

    for fish in fish_list:
        if fish[3] == 1: # status [y,x,d,stats,cnt]
            fishes.append(copy(fish))

    return fishes


def move_fishes():
    """
    2. 모든 물고기 한 칸씩 이동
      - 상어, 물고기 냄새, 격자 범위 외 칸 이동 불가
      - 이동할 수 있을때까지 방향 45 반시계 회전
      - 이동할 칸이 없다면 이동 x
    """

    for idx, fish in enumerate(fish_list):
        # 이동 가능 유무 식별
        if fish[3] != 1:
            continue

        ny, nx, nd = fish[0], fish[1], fish[2]
        dir_cnt = 0
        for i in range(8 + 1):
            dir_cnt += 1
            can_move = True

            nd = (fish[2] - i) % 8
            ny = fish[0] + fdy[nd]
            nx = fish[1] + fdx[nd]

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue

            next_area = board[ny][nx]

            # 이동 영역이 비어 있다면 이동 가능
            if not next_area:
                break

            # 물고기 냄새나 상어가 있다면 이동 불가능
            for na_fish in next_area:
                if na_fish[3] == 0 or na_fish[3] == 2:
                    can_move = False
                    break

            if can_move is False:
                continue

            break

        if nd == fish[2] and dir_cnt > 1:
            continue

        fish[0] = ny
        fish[1] = nx
        fish[2] = nd

    _set_board()


def move_shark():
    """
    3. 상어 3칸 연속 이동
      - 가능한 이동 방향 중 물고기의 수가 가장 많은 방법 선택
        (방법이 여러가지인 경우, 사전순 가장 앞서는 방법)
      - 상하좌우 이동
      - 물고기를 만나면 해당 칸 물고기 전부 제외 -> 물고기 냄새
    """

    route: List[int] = find_route()

    if not route:
        return

    ny, nx = shark[0], shark[1]

    rm_set = set()

    for d in route:
        ny = ny + sdy[d]
        nx = nx + sdx[d]

        next_area = board[ny][nx]
        for na_fish in next_area:
            if na_fish[3] == 1:
                rm_set.add((na_fish[0], na_fish[1]))

    # 상위 위치 변경
    shark[0] = ny
    shark[1] = nx

    # 물고기 상태 변경
    for y, x in rm_set:
        for fish in fish_list:
            if fish[0] == y and fish[1] == x and fish[3] == 1:
                fish[3] = 2

    # 물고기 좌표 갱신
    _set_board()


def find_route():
    route_list = []
    rm_list = []
    max_rm_cnt = 0

    # 경로별 상어 이동시 제거 가능 물고기 수 및 경로 확인
    for route in shark_route_list:
        new_board = deepcopy(board)

        # 범위 유효성 검증
        ny, nx, nd = shark[0], shark[1], shark[2]
        valid_route = True
        for direct in route:
            ny = ny + sdy[direct]
            nx = nx + sdx[direct]

            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                valid_route = False
                break

        if not valid_route:
            continue

        # 연속 3칸 이동 시뮬레이션
        ny, nx = shark[0], shark[1]
        rm_cnt = 0

        for direct in route:  # 3번 이동
            ny = ny + sdy[direct]
            nx = nx + sdx[direct]

            next_area = new_board[ny][nx]

            if not next_area:
                continue

            for na_fish in next_area:
                if na_fish[3] == 1:  # 물고기
                    rm_cnt += 1

            new_board[ny][nx] = []

        route_list.append(route)
        rm_list.append(rm_cnt)
        max_rm_cnt = max(max_rm_cnt, rm_cnt)

    # 최대 물고기 획득 가능 경로 목록
    max_rm_route_list = []
    for idx, route in enumerate(route_list):
        if rm_list[idx] == max_rm_cnt:
            max_rm_route_list.append(route)

    if not max_rm_route_list:
        return []

    return max_rm_route_list[0]


def remove_fish_smell():
    global fish_list

    new_fish_list = []

    for fish in fish_list:
        if fish[4] != 2:
            new_fish_list.append(fish)

    fish_list = new_fish_list


def _set_board():
    global board
    new_board: List[List[List[Node]]] = [[[] for _ in range(4)] for _ in range(4)]

    for fish in fish_list:
        new_board[fish[0]][fish[1]].append(fish)

    new_board[shark[0]][shark[1]].append(shark)

    board = new_board


def _set_shark_route_list(depth: int, dirs: str, last_depth=3):
    global shark_route_list
    """
    상어 이동 경로를 초기화하는 함수
    전역 변수 shark_route_list  초기화
    """

    # 종료 조건
    if depth == last_depth:
        dir_list = list(map(lambda x: x - 1, list(map(int, list(dirs)))))

        shark_route_list.append(dir_list)
        return

    for i in range(1, 4 + 1):
        _set_shark_route_list(depth + 1, dirs + str(i))


init()

"""
0. 물고기 냄새 카운트 증가
1. 물고기 복제
- 지연시간 대기 후 5단계에서 복제됨
2. 모든 물고기 한 칸씩 이동
  - 상어, 물고기 냄새, 격자 범위 외 칸 이동 불가
  - 이동할 수 있을때까지 방향 45회전
  - 이동할 칸이 없다면 이동 x
3. 상어 3칸 연속 이동
  - 가능한 이동 방향 중 물고기의 수가 가장 많은 방법 선택
    (방법이 여러가지인 경우, 사전순 가장 앞서는 방법)
  - 상하좌우 이동
  - 물고기를 만나면 해당 칸 물고기 전부 제외 -> 물고기 냄새
4. 2 번 전 물고기의 냄새는 사라진다.
5. 1에서의 복제마법 완료
"""

for _ in range(s):
    # 냄새 카운트
    count_fish_smell()

    # 물고기 복제
    cpy_fish_list = copy_fish()

    # 물고기 이동
    move_fishes()

    # 상어 이동
    move_shark()

    # 물고기 냄새 제거
    remove_fish_smell()

    # 복제 완료
    fish_list = fish_list + cpy_fish_list
    _set_board()

fish_cnt = 0
for i in range(n):
    for j in range(n):
        for fish in board[i][j]:
            if fish[3] == 1:
                fish_cnt += 1

print(fish_cnt)
