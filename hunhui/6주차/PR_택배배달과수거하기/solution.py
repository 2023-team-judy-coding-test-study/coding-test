from collections import deque

def solution(cap, n, deliveries, pickups):
    answer = 0
    dQue, pQue = deque(), deque()
    
    for i in range(n):
        dc, pc = deliveries[i], pickups[i]
        for _ in range(dc):
            dQue.append(i+1)
        for _ in range(pc):
            pQue.append(i+1)
    
    while dQue or pQue:
        maxDistance = 0
        # 배달
        for i in range(cap):
            if not dQue:
                break
            maxDistance = max(maxDistance, dQue.pop())
        # 수거
        for i in range(cap):
            if not pQue:
                break
            maxDistance = max(maxDistance, pQue.pop())
        answer += maxDistance*2
    
    return answer