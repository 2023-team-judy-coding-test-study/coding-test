#python3는 시간초과 pypy3는 통과
from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

tmp = list(map(int, input().split()))
belts = [[x for x in tmp[:N]], [x for x in tmp[-1:N-1:-1]]]
dv = [(-1,0), (0,1), (1,0), (0,-1)]

def beltMove(belts,  N):
    queue = deque([(0, 0, belts[0][0])])
    belts[0][0] = belts[1][0]
    d = 1
    while queue:
        x, y, data = queue.popleft()

        if x == 1 and y == 0: continue

        for _ in range(4):
            nx, ny = x + dv[d][0], y + dv[d][1]
            if nx < 0 or nx >= 2 or ny < 0 or ny >= N:
                d = (d+1)%4
                continue

            queue.append((nx, ny, belts[nx][ny]))
            belts[nx][ny] = data
            break


def robotMove(robots, belts, N):
    queue = deque()

    for i in range(N-2, -1, -1):
        if robots[i] == 1:
            queue.append(i)

    while queue:
        y = queue.popleft()

        ny = y + 1

        if belts[0][ny] > 0 and robots[ny] == 0:
            belts[0][ny] -= 1
            robots[y] = 0
            robots[ny] = 1
            if ny == (N - 1): robots[ny] = 0

count = 1
robots = [0] * N
robots = deque(robots)
while True:
    beltMove(belts, N)
    robots.rotate(1)
    robots[N-1] = 0

    robotMove(robots, belts, N)

    if belts[0][0] > 0:
        belts[0][0] -= 1
        robots[0] = 1

    if belts[0].count(0) + belts[1].count(0) >= K: break
    count += 1

print(count)