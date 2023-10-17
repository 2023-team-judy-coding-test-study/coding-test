import sys

input = sys.stdin.readline


dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

board = []
dice = [0] * 6


class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x


def main():
    global board, dice, dy, dx
    """
    지도의 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20), 
    주사위를 놓은 곳의 좌표 x, y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1), 
    명령의 개수 K (1 ≤ K ≤ 1,000)

    둘째 줄부터 N개의 줄에 지도에 쓰여 있는 수가 북쪽부터 남쪽으로, 
    각 줄은 서쪽부터 동쪽 순서대로 주어진다. 
    주사위를 놓은 칸에 쓰여 있는 수는 항상 0이다. 
    지도의 각 칸에 쓰여 있는 수는 10 미만의 자연수 또는 0이다.
    
    참고: https://velog.io/@sin5015243/%EB%B0%B1%EC%A4%80-14499-%EC%A3%BC%EC%82%AC%EC%9C%84-%EA%B5%B4%EB%A6%AC%EA%B8%B0-Python
    """
    # 초기화
    n, m, x, y, k = map(int, input().split())

    for _ in range(n):
        row = list(map(int, input().split()))

        board.append(row)

    cmd_list = list(map(int, input().split()))

    now = Node(y, x)
    # 주사위 굴리기
    for c in cmd_list:
        nx = now.x + dr[c]
        ny = now.y + dc[c]
        if ny < 0 or nx < 0 or ny >= m or nx >= n:
            continue

        east, west, south, north, up, down = dice[0], dice[1], dice[2], dice[3], dice[4], dice[5]

        # east
        if c == 1:
            dice[0], dice[1], dice[4], dice[5] = down, up, east, west
        # west
        elif c == 2:
            dice[0], dice[1], dice[4], dice[5] = up, down, west, east
        # north
        elif c == 3:
            dice[2], dice[3], dice[4], dice[5] = up, down, north, south
        # south
        elif c == 4:
            dice[2], dice[3], dice[4], dice[5] = down, up, south, north
        else:
            continue

        # 주사위 바닥면 -> 칸 숫자 복사
        if board[nx][ny] == 0:
            board[nx][ny] = dice[5]

        # 칸 -> 주사위 바닥면 숫자 복사
        else:
            dice[5] = board[nx][ny]
            board[nx][ny] = 0

        now = Node(ny, nx)
        print(dice[4])


if __name__ == "__main__":
    main()
