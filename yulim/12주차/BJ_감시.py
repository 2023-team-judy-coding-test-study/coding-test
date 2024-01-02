#3:25

import copy


       
N, M = map(int, input().split())
maps = [[int(x) for x in input().split()] for _ in range(N)]

# 북동남서
dv = [(-1, 0), (0,1), (1, 0), (0, -1)]

cctv_directions = {1: [[0], [1], [2], [3]],
                   2: [[1, 3], [0, 2]],
                   3: [[0, 1], [1, 2], [2, 3], [3, 0]],
                   4: [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
                   5: [[0, 1, 2, 3]]}

min_value = 1e9

cctv = []            
for i in range(N):
    for j in range(M):
        if 0 < maps[i][j] < 6:  # 카메라가 있으면
            cctv.append((i, j, maps[i][j])) # x, y, 카메라 정보

def find_sight(m, directions, x, y):
    for d in directions:
        nx = x
        ny = y
        while True:
            nx += dv[d][0]
            ny += dv[d][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or m[nx][ny] == 6:
                break
            elif m[nx][ny] == 0:
                m[nx][ny] = -1


def dfs(depth, m):
    global min_value
    if depth == len(cctv):
        count = 0
        for mm in m:  # 0 개수 세기(사각지대 수)
            count += mm.count(0)
        min_value = min(min_value, count)
        return
    
    tmp_maps = copy.deepcopy(m)
    x, y, n = cctv[depth]

    for directions in cctv_directions[n]:
        find_sight(tmp_maps, directions, x, y)
        dfs(depth+1, tmp_maps)
        tmp_maps = copy.deepcopy(m) # 보드 초기화

dfs(0, maps)
print(min_value)

