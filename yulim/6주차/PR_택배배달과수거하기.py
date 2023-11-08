# 그리디
# 먼 곳 부터 탐색

def solution(cap, n, deliveries, pickups):
    answer = 0
    
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    deliver = 0
    pickup = 0

    for i in range(n):

        deliver += deliveries[i]
        pickup += pickups[i]

        while deliver > 0 or pickup > 0:
            deliver -= cap
            pickup -= cap
            answer += (n - i) * 2
    
    return answer


print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))

