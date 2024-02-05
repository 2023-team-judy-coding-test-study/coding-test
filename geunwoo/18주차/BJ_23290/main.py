import sys

from typing import *
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
# 0, 1, 2, 3, 4 ,5, 6, 7
# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dy = [0, -1, -1, -1, 0, 1, 1, 1]
dx = [-1, -1, 0, 1, 1, 1, 0, -1]

# shark 상은 1, 좌는 2, 하는 3, 우는 4로 변환
sy = [-1, 0, 1, 0]
sx = [0, -1, 0, 1]

board = [[[] for _ in range(4)] for _ in range(4)]

path_dict = {}
max_dead_fish_cnt = 0


def main():
    global board

    m, s = map(int, input().split())

    # 초기화 - 물고기 위치
    fish_list = [list(map(int, input().split())) for _ in range(m)]

    for y, x, d in fish_list:
        board[y-1][x-1].append(d - 1)

    # 초기화 - 상어 위치
    shark = tuple(map(lambda x: int(x) - 1, input().split()))
    smell_list = [[0] * 4 for _ in range(4)]

    for _ in range(s):
        eat = []
        max_eat = -1

        # 상어 복제
        cpy_board = deepcopy(board)
        shark_copy_magic(cpy_fish_dict)

        # 모든 물고기 이동
        # print("모든 물고기 이동\n")
        # print(f"shark: ({shark.y}, {shark.x})")
        move_all_fish(fish_dict, shark)
        # for row in board:
        # print(row)
        # print()

        # 상어 연속 3칸 이동
        # print("상어 연속 3칸 이동")
        move_shark(fish_dict, shark)
        # print(f"shark: ({shark.y}, {shark.x})\n")
        # for row in board:
        # print(row)
        # print()

        # 두번 전 연습에서 생긴 물고기 냄새 제거
        remove_dead_fish(fish_dict)
        # print(f"물고기 냄새 제거\n fish_dict {fish_dict}\n")

        # 상어 복제 마법 완료
        finish_shark_magic(fish_dict, cpy_fish_dict)
        # print(f"상어 복제 마법 완료")
        # for row in board:
        # print(row)
        # print()
    fish_cnt = count_fish()
    print(fish_cnt)


def shark_copy_magic(fish_dict: Dict[int, Node]):
    global board

    for i in range(4):
        for j in range(4):
            for idx, fish in board[i][j].items():
                if fish.is_dead is False:
                    fish_dict[fish.i] = fish


def generate_index(fish_dict: Dict[int, Node], idx: int = None):
    if idx and not idx_exist(idx + 1, fish_dict):
        return idx + 1

    last_idx = 0
    fish_keys: list = list(fish_dict.keys())

    if not fish_keys:
        return last_idx

    fish_keys.sort()
    last_idx = fish_keys[-1]

    return last_idx + 1


def idx_exist(idx: int, fish_dict: Dict[int, Node]):

    if fish_dict.get(idx):
        return True

    return False


def move_all_fish(fish_dict: Dict[int, Node], shark: Node):
    global board
    for i, fish in fish_dict.items():
        if fish.is_dead:
            continue

        ny, nx, direction = fish.y, fish.x, fish.d

        # 이동 방향 설정
        for i in range(9):
            ny = fish.y + dy[direction]
            nx = fish.x + dx[direction]

            if can_move(ny, nx, shark):
                # 물고기 이동
                del board[fish.y][fish.x][fish.i]
                fish = Node(fish.i, ny, nx, direction)

                board[ny][nx][fish.i] = fish
                fish_dict[fish.i] = fish

                break
            else:
                direction = (direction - 1) % 8


def can_move(ny, nx, shark: Node):
    global board

    if ny < 0 or nx < 0 or ny >= 4 or nx >= 4:
        return False

    if ny == shark.y and nx == shark.x:
        return False

    for i, fish in board[ny][nx].items():
        if fish.is_dead:
            return False

    return True


def move_shark(fish_dict: Dict[int, Node], shark: Node):
    global board, path_dict

    path_dict = {}
    select_shark_path(1, "", shark, fish_dict)
    path: str = path_dict[sorted(list(path_dict.keys()))[-1]]

    dir_list = list(map(int, list(path)))
    ny, nx = shark.y, shark.x
    # print(f"path, {path}")

    for i, fish in board[ny][nx].items():
        if not fish.is_dead:
            fish.is_dead = True
            fish_dict[fish.i].is_dead = True

    for d in dir_list:
        ny = ny + sy[d-1]
        nx = nx + sx[d-1]

        for i, fish in board[ny][nx].items():
            if not fish.is_dead:
                fish.is_dead = True
                fish_dict[fish.i].is_dead = True

    shark.y = ny
    shark.x = nx


def select_shark_path(depth: int, dirs: str, shark: Node, fish_dict: Dict[int, Node]):
    global board
    if depth > 3:
        cpy_board = deepcopy(board)
        cpy_fish_dict = deepcopy(fish_dict)
        check_shark_path(dirs, shark, cpy_board, cpy_fish_dict)

        return

    for d in range(1, 4 + 1):
        select_shark_path(depth+1, dirs+str(d), shark, fish_dict)


def check_shark_path(dirs: str, shark: Node, board: List[List[int]], fish_dict: Dict[int, Node]):
    global path_dict
    dead_fish_cnt = 0

    dir_list = list(map(int, list(dirs)))

    ny, nx = shark.y, shark.x

    for _, fish in board[ny][nx].items():
        if not fish.is_dead:
            dead_fish_cnt += 1
            fish.is_dead = True
            fish_dict[fish.i].is_dead = True

    for d in dir_list:
        ny = ny + sy[d-1]
        nx = nx + sx[d-1]

        if ny < 0 or nx < 0 or ny >= 4 or nx >= 4:
            return False

        for i, fish in board[ny][nx].items():
            if not fish.is_dead:
                dead_fish_cnt += 1
                fish.is_dead = True
                fish_dict[fish.i].is_dead = True

    if not path_dict.get(dead_fish_cnt):
        path_dict[dead_fish_cnt] = dirs

    return True


def remove_dead_fish(fish_dict: Dict[int, Node]):
    fish_idx_list = []

    for i, fish in fish_dict.items():
        if fish.is_dead:
            fish.dead_cnt += 1

        if fish.dead_cnt >= 3:
            fish_idx_list.append(fish.i)

    for idx in fish_idx_list:
        del fish_dict[idx]


def finish_shark_magic(fish_dict: Dict[int, Node], cpy_fish_dict: Dict[int, Node]):
    global board

    for i, fish in cpy_fish_dict.items():
        new_idx: int = generate_index(fish_dict=fish_dict)
        new_fish = Node(new_idx, fish.y, fish.x, fish.d)

        fish_dict[new_idx] = new_fish

        board[fish.y][fish.x][new_idx] = new_fish


def count_fish():
    global board
    cnt = 0

    for i in range(4):
        for j in range(4):
            for idx, fish in board[i][j].items():
                if not fish.is_dead:
                    cnt += 1

    return cnt


if __name__ == "__main__":
    main()
