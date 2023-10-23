import sys
input = sys.stdin.readline

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]


n: int
board = []
result = 0


class Node:
    def __init__(self, y, x, level):
        self.y = y
        self.x = x
        self.level = level


def main():
    global n, board, result

    n = int(input())
    for i in range(n):
        row = list(map(int, input().split()))

        board.append(row)

    start = Node(int(n/2), int(n/2), 0)

    # spiral
    move_spiral(start)

    print(result)


def move_spiral(start: Node):
    global n, board

    now = Node(start.y, start.x, start.level+1)

    dir_cnt = 1
    direction = 0
    while True:
        if now.y == 0 and now.x == 0:
            break

        for _ in range(2):
            cnt = 0
            while cnt < dir_cnt:
                if now.y == 0 and now.x == 0:
                    break

                ny = now.y + dy[direction]
                nx = now.x + dx[direction]

                # 모래 합치기
                board[ny][nx] += board[now.y][now.x]
                board[now.y][now.x] = 0

                cnt += 1
                now = Node(ny, nx, now.level + 1)

                # 모래 주변에 뿌리기
                spread_sand(now, direction)

            direction = (direction+1) % 4

        dir_cnt += 1


def spread_sand(pos: Node, direction: int):
    global board, result

    sand: int = board[pos.y][pos.x]
    sep_sand = 0
    if direction == 0:
        # 5%
        sep_sand += cal_sand(ny=pos.y, nx=pos.x-2, rate=5, sand=sand)
        # 10%0
        sep_sand += cal_sand(ny=pos.y+1, nx=pos.x-1, rate=10, sand=sand)
        sep_sand += cal_sand(ny=pos.y-1, nx=pos.x-1, rate=10, sand=sand)
        # 7%
        sep_sand += cal_sand(ny=pos.y+1, nx=pos.x, rate=7, sand=sand)
        sep_sand += cal_sand(ny=pos.y-1, nx=pos.x, rate=7, sand=sand)
        # 1%
        sep_sand += cal_sand(ny=pos.y+1, nx=pos.x+1, rate=1, sand=sand)
        sep_sand += cal_sand(ny=pos.y-1, nx=pos.x+1, rate=1, sand=sand)
        # 2%
        sep_sand += cal_sand(ny=pos.y+2, nx=pos.x, rate=2, sand=sand)
        sep_sand += cal_sand(ny=pos.y-2, nx=pos.x, rate=2, sand=sand)

        sand -= sep_sand
        ny = pos.y
        nx = pos.x - 1

    if direction == 1:
        # 5%
        sep_sand += cal_sand(ny=pos.y+2, nx=pos.x, rate=5, sand=sand)
        # 10%
        sep_sand += cal_sand(ny=pos.y+1, nx=pos.x-1, rate=10, sand=sand)
        sep_sand += cal_sand(ny=pos.y+1, nx=pos.x+1, rate=10, sand=sand)
        # 7%
        sep_sand += cal_sand(ny=pos.y, nx=pos.x-1, rate=7, sand=sand)
        sep_sand += cal_sand(ny=pos.y, nx=pos.x+1, rate=7, sand=sand)
        # 1%
        sep_sand += cal_sand(ny=pos.y-1, nx=pos.x-1, rate=1, sand=sand)
        sep_sand += cal_sand(ny=pos.y-1, nx=pos.x+1, rate=1, sand=sand)
        # 2%
        sep_sand += cal_sand(ny=pos.y, nx=pos.x-2, rate=2, sand=sand)
        sep_sand += cal_sand(ny=pos.y, nx=pos.x+2, rate=2, sand=sand)

        sand -= sep_sand
        ny = pos.y + 1
        nx = pos.x

    if direction == 2:
        # 5%
        sep_sand += cal_sand(ny=pos.y, nx=pos.x+2, rate=5, sand=sand)
        # 10%
        sep_sand += cal_sand(ny=pos.y+1, nx=pos.x+1, rate=10, sand=sand)
        sep_sand += cal_sand(ny=pos.y-1, nx=pos.x+1, rate=10, sand=sand)
        # 7%
        sep_sand += cal_sand(ny=pos.y+1, nx=pos.x, rate=7, sand=sand)
        sep_sand += cal_sand(ny=pos.y-1, nx=pos.x, rate=7, sand=sand)
        # 1%
        sep_sand += cal_sand(ny=pos.y+1, nx=pos.x-1, rate=1, sand=sand)
        sep_sand += cal_sand(ny=pos.y-1, nx=pos.x-1, rate=1, sand=sand)
        # 2%
        sep_sand += cal_sand(ny=pos.y+2, nx=pos.x, rate=2, sand=sand)
        sep_sand += cal_sand(ny=pos.y-2, nx=pos.x, rate=2, sand=sand)

        sand -= sep_sand
        ny = pos.y
        nx = pos.x + 1

    if direction == 3:
        # 5%
        sep_sand += cal_sand(ny=pos.y-2, nx=pos.x, rate=5, sand=sand)
        # 10%
        sep_sand += cal_sand(ny=pos.y-1, nx=pos.x-1, rate=10, sand=sand)
        sep_sand += cal_sand(ny=pos.y-1, nx=pos.x+1, rate=10, sand=sand)
        # 7%
        sep_sand += cal_sand(ny=pos.y, nx=pos.x-1, rate=7, sand=sand)
        sep_sand += cal_sand(ny=pos.y, nx=pos.x+1, rate=7, sand=sand)
        # 1%
        sep_sand += cal_sand(ny=pos.y+1, nx=pos.x-1, rate=1, sand=sand)
        sep_sand += cal_sand(ny=pos.y+1, nx=pos.x+1, rate=1, sand=sand)
        # 2%
        sep_sand += cal_sand(ny=pos.y, nx=pos.x-2, rate=2, sand=sand)
        sep_sand += cal_sand(ny=pos.y, nx=pos.x+2, rate=2, sand=sand)

        sand -= sep_sand
        ny = pos.y - 1
        nx = pos.x

    if is_in(ny, nx):
        board[ny][nx] += sand
    else:
        result += sand
    board[pos.y][pos.x] = 0


def cal_sand(ny: int, nx: int, rate: int, sand: int):
    global board, result

    sep_sand = int(sand*rate/100)

    if is_in(ny, nx) is True:
        board[ny][nx] += sep_sand
    else:
        result += sep_sand

    return sep_sand


def is_in(y, x):
    return y >= 0 and x >= 0 and y < n and x < n


if __name__ == "__main__":
    main()
