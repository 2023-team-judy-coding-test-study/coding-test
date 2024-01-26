# 11:24
import math
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def is_in(x, y, d1, d2):
    return y-d1 > 0 and x+d1+d2 <= n and y+d2 <= n

def is_num_five(x, y, d1, d2, r, c):
    up = y
    down = y
    if r == x:
        if up <= c <= down:
            return True
        else:
            return False
    for i in range(1, d1+d2+1):
        if i <= d1:
            up -= 1
        else:
            up += 1
        if i <= d2:
            down += 1
        else:
            down -= 1
        if r == x+i:
            if up <= c <= down:
                return True
            else:
                return False
    return False

def get_num(x, y, d1, d2, r, c):
    if is_num_five(x, y, d1, d2, r, c):
        return 5
    if 1 <= r <= x+d1 and 1 <= c < y:
        return 1
    if x+d1 < r <= n and 1 <= c <= y-d1+d2:
        return 2
    if 1 <= r < x+d2 and y <= c <= n:
        return 3
    return 4

answer = math.inf
for y in range(1, n+1):
    for x in range(1, n+1):
        for d1 in range(1, n+1):
            for d2 in range(1, n+1):
                if not is_in(x, y, d1, d2):
                    continue
                li = [0]*5
                temp = [[0]*n for _ in range(n)]
                for c in range(1, n+1):
                    for r in range(1, n+1):
                        num = get_num(x, y, d1, d2, r, c)-1
                        li[num] += grid[c-1][r-1]
                        temp[c-1][r-1] = num
                answer = min(max(li) - min(li), answer)
print(answer)