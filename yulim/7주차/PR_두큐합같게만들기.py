from collections import deque

def solution(queue1, queue2):
    
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    div = (sum1 + sum2)//2
        
    cnt = 0
    for x in range(300000):
        if(sum1 > div):
            sum1 -= queue1[0]
            sum2 += queue1[0]
            queue2.append(queue1.popleft())
            cnt += 1

        elif(sum2 > div):
            sum1 += queue2[0]
            sum2 -= queue2[0]
            queue1.append(queue2.popleft())
            cnt += 1
            
        else:
            return cnt
            
    return -1