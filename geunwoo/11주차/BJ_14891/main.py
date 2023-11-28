import sys

from collections import deque
from typing import List

input = sys.stdin.readline

valid_gear_list = [1, 2, 3, 4]
LEFT_DIRECT = -1
RIGHT_DIRECT = 1

def main():
    # init
    gears = [[]]

    for _ in range(4):
        gear = list(map(int, list(input().strip())))
        gears.append(gear)

    n = int(input())

    for _ in range(n):
        num, rotate_direction = map(int, input().split())

        # rotate left gear
        gears = rotate_gear(gears, num - 1, -rotate_direction, LEFT_DIRECT)

        # rotate right gear
        gears = rotate_gear(gears, num + 1, -rotate_direction, RIGHT_DIRECT)

        # rotate
        gears = rotate_gear(gears, num, rotate_direction)

    cnt = 0
    if gears[1][0] == 1:
        cnt += 1
    if gears[2][0] == 1:
        cnt += 2
    if gears[3][0] == 1:
        cnt += 4
    if gears[4][0] == 1:
        cnt += 8

    print(cnt)



def rotate_gear(gears: List[List[int]], num: int, rotate_direction=1, has_effect_direct=0):

    if check_valid_gear(num) is False:
        return gears

    if has_effect_direct == LEFT_DIRECT:
        if check_valid_gear(num+1) and gears[num][2] == gears[num+1][6]:
            return gears
        elif check_valid_gear(num+1) and gears[num][2] != gears[num+1][6]:
            gears = rotate_gear(gears, num + has_effect_direct, -rotate_direction, has_effect_direct)

    if has_effect_direct == RIGHT_DIRECT:
        if check_valid_gear(num-1) and gears[num][6] == gears[num-1][2]:
            return gears
        elif check_valid_gear(num - 1) and gears[num][6] != gears[num - 1][2]:
            gears = rotate_gear(gears, num + has_effect_direct, -rotate_direction, has_effect_direct)

    q = deque(gears[num])
    q.rotate(rotate_direction)

    gears[num] = list(q)

    return gears


def check_valid_gear(gear_num: int):

    if gear_num in valid_gear_list:
        return True

    return False


if __name__ == '__main__':
    main()




