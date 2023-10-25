from typing import *

max_depth = 0
a_info = []
max_info = []
max_score_diff = 0


def solution(n: int, info: List[int]):
    global max_depth, a_info
    
    max_depth = n
    a_info = info
    init_info = [0] * 11
    select_score(0, init_info, 0)
    return max_info if max_score_diff > 0 else [-1]
    

def select_score(depth: int, l_info: List[int], idx:int):
    global max_depth, a_info, max_info, max_score_diff
    if depth == max_depth:
        l_score = 0
        a_score = 0
        for i in range(0, 10 + 1):
            if l_info[i] > a_info[i]:
                l_score += (10 - i)
            elif a_info[i] != 0:
                a_score += (10 - i)
            
            score_diff = l_score - a_score
            
        if score_diff > max_score_diff or max_score_diff == 0:
            max_info = l_info
            max_score_diff = score_diff
        elif max_score_diff > 0 and max_score_diff == score_diff:
            for i in range(10, -1, -1):
                if l_info[i] > max_info[i]:
                    max_info = l_info
                elif max_info[i] > l_info[i]:
                    return
        return
    
    for i in range(idx, 10 + 1):
        next_info = [l_info[i] for i in range(11)]
        
        if i == 10:
            next_info[i] = max_depth - depth
            select_score(max_depth, next_info, idx+1)
            
        elif max_depth - depth > a_info[i]:
            next_info[i] = a_info[i] + 1
            select_score(depth + next_info[i], next_info, idx+1)
        