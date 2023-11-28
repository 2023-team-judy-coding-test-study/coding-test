import sys
from typing import List

input = sys.stdin.readline

slope = []

def main():
    global slope
    n, l = map(int, input().split())

    board = []
    for i in range(n):
        row = list(map(int, input().strip().split()))
        board.append(row)

    cnt = 0
    for i in range(n):
        slope = [False] * n
        row = board[i]
        if is_street(row, n, l):
            cnt += 1

        slope = [False] * n
        col = [board[j][i] for j in range(n)]
        if is_street(col, n, l):
            cnt += 1

    print(cnt)


def is_street(line: List[int], n: int, l: int):
    global slope
    for i in range(1, n):
        if abs(line[i] - line[i - 1]) > 1:
            return False

        # 내리막 길
        if line[i] < line[i - 1]:
            for j in range(l):
                if i + j >= n or line[i] != line[i+j] or slope[i+j]:
                    return False

                slope[i+j] = True
        elif line[i] > line[i - 1]:
            for j in range(l):
                if i - j - 1 < 0 or line[i - 1] != line[i - j - 1] or slope[i - j - 1]:
                    return False

                slope[i - j - 1] = True

    return True


if __name__ == '__main__':
    main()
