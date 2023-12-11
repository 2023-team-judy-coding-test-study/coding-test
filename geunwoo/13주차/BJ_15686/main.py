import sys
from typing import List

input = sys.stdin.readline


class Point:
    def __init__(self, y, x):
        self.y = y
        self.x = x

    def __str__(self):
        return f"({self.y}, {self.x})"


def main():
    """
    도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시켜야 한다.
    어떻게 고르면, 도시의 치킨 거리가 가장 작게 될지 구하는 프로그램을 작성하시오.
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2
    """

    selected_chicken: List[Point] = []
    answer = int(1e9)

    def select_chicken(idx: int, level: int):
        nonlocal selected_chicken, answer

        # 종료 시점
        if level >= m:
            sum_num = 0
            for home in home_list:
                min_distance = int(1e9)
                for chicken in selected_chicken:
                    min_distance = min(min_distance, abs(home.y - chicken.y) + abs(home.x - chicken.x))
                sum_num += min_distance
            answer = min(answer, sum_num)
            return

        # 가지 치기
        for idx in range(idx, len(chicken_list)):
            selected_chicken.append(chicken_list[idx])
            select_chicken(idx + 1, level + 1)
            selected_chicken.pop()

    n, m = map(int, input().split())

    board = []
    home_list: List[Point] = []
    chicken_list: List[Point] = []
    for i in range(n):
        raw = list(map(int, input().split()))

        for j in range(n):
            if raw[j] == 1:
                home_list.append(Point(i, j))
            elif raw[j] == 2:
                chicken_list.append(Point(i, j))
        board.append(raw)

    select_chicken(0, 0)

    print(answer)


if __name__ == "__main__":
    main()
