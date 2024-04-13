
dy = [ 0, 0,-1, 1]
dx = [-1, 1, 0, 0]

t = 0
n = 0
board = []
core_list = []
c_l = 0
max_core_cnt = 0
min_tot_len = 1e9


def back(depth, tot_len, core_cnt):
    global n, core_list, c_l, min_tot_len, max_core_cnt

    if depth == c_l:
        if core_cnt > max_core_cnt:
            max_core_cnt = core_cnt
            min_tot_len = tot_len
        elif core_cnt == max_core_cnt and min_tot_len > tot_len:
            min_tot_len = tot_len

        return

    for i in range(depth, c_l):
        cy, cx = core_list[i]
        for d in range(4):
            ny = cy
            nx = cx

            can_move = False
            path = set()
            leng = 0

            while True:
                ny = ny + dy[d]
                nx = nx + dx[d]

                if ny < 0 or nx < 0 or ny >= n or nx >= n:
                    can_move = True
                    break

                if board[ny][nx] == 1:
                    break

                path.add((ny, nx))
                leng += 1

            if can_move:
                for py, px in path:
                    board[py][px] = 1

                back(i+1, tot_len+leng, core_cnt+1)

                for py, px in path:
                    board[py][px] = 0


def main():
    global t, n, board, core_list, c_l, min_tot_len
    """
    7 <= n <= 12
    max 16,777,216
    1. Core 선택
    2. 방향 선택
    3. 전선 깔기
    """
    t = int(input())
    # init
    for num in range(1, t+1):
        n = int(input())
        min_tot_len = 1e9

        board = []
        core_list = []
        for i in range(n):
            row = list(map(int, input().split()))

            for j in range(1, n-1):
                if i == 0 or i == n-1:
                    break

                if row[j] == 1:
                    core_list.append((i, j))

            board.append(row)

        c_l = len(core_list)
        # 전선 설치
        back(0, 0, 0)

        # 출력
        print(f"#{num} {min_tot_len}")


if __name__ == '__main__':
    main()
