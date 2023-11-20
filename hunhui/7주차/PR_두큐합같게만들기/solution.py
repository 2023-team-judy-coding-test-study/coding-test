from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    
    s1 = sum(queue1)
    s2 = sum(queue2)
    
    count = 0
    lenSum = len(queue1) + len(queue2)
    
    while s1 != s2:
        if count > lenSum + 10:
            count = -1
            break
        count += 1
        if s1 > s2:
            n = q1.popleft()
            q2.append(n)
            s1 -= n
            s2 += n
        else:
            n = q2.popleft()
            q1.append(n)
            s2 -= n
            s1 += n
    
    return count