import sys

from collections import deque
from functools import reduce
from typing import List

input = sys.stdin.readline


class Room:
    def __init__(self, durability, robot):
        self.durability = durability
        self.robot = robot

    def __str__(self):
        return f"durability: {self.durability}, robot: {self.robot}"

    def __repr__(self):
        return f"({self.durability}, {self.robot})"

def main():
    # init
    n, k = map(int, input().split())

    c_belt = list(map(int, input().split()))

    conveyor_belt: List[Room] = []
    for durability in c_belt:
        conveyor_belt.append(Room(durability, False))

    stage = 0
    while True:
        stage += 1

        # 벨트 회전 한다.
        q = deque(conveyor_belt)
        q.rotate()
        conveyor_belt = list(q)

        # 로봇 이동 한다.
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                conveyor_belt[i].robot = False
                continue

            if conveyor_belt[i].robot is False:
                continue

            # 이동할 칸의 내구도가 0보다 크고, 로봇이 존재하지 않는다면 이동한다.
            if conveyor_belt[i + 1].durability > 0 and conveyor_belt[i + 1].robot is False:
                conveyor_belt[i].robot = False
                conveyor_belt[i + 1].durability -= 1
                conveyor_belt[i + 1].robot = True

        if conveyor_belt[n-1].robot is True:
            conveyor_belt[n - 1].robot = False

        # 로봇 올린다
        if conveyor_belt[0].durability > 0 and conveyor_belt[0].robot is False:
            conveyor_belt[0].durability -= 1
            conveyor_belt[0].robot = True

        cnt = 0
        for room in conveyor_belt:
            if room.durability == 0:
                cnt += 1

        if cnt >= k:
            break

    print(stage)


if __name__ == '__main__':
    main()
