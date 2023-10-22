from typing import *


def solution(cap: int, n: int, deliveries: List[int], pickups: List[int]):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    have_to_deli = 0
    have_to_pick = 0

    answer = 0
    for i in range(n):
        have_to_deli += deliveries[i]
        have_to_pick += pickups[i]

        while have_to_deli > 0 or have_to_pick > 0:
            have_to_deli -= cap
            have_to_pick -= cap

            answer += (n-i) * 2

    return answer
