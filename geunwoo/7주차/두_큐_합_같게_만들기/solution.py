from typing import *
from collections import deque


def solution(queue1: List[int], queue2: List[int]):
    q_1_sum = sum(queue1)
    q_2_sum = sum(queue2)
    q_1_size = len(queue1)
    q_2_size = len(queue2)

    q_sum = q_1_sum + q_2_sum
    q_size = q_1_size + q_2_size

    # 목표 값 구하기
    if q_sum % 2 != 0:
        return -1
    goal = int(q_sum/2)

    q1 = deque(queue1)
    q2 = deque(queue2)

    cnt = 0
    limit = q_size * 2  # 큐의 길이만큼만 loop를 순회할 경우 실패하는 테스트 케이스가 존재
    while q_1_sum != q_2_sum and cnt <= limit:

        element = 0
        if q_1_sum < q_2_sum:
            element = q2.popleft()
            q1.append(element)

            q_1_sum += element
            q_2_sum -= element

        elif q_1_sum > q_2_sum:
            element = q1.popleft()
            q2.append(element)

            q_1_sum -= element
            q_2_sum += element
        else:
            break

        cnt += 1

    if cnt >= limit:
        return -1

    return cnt
