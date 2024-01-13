# 5:11 ~ 7:03 (1'52")

N = int(input())
maps = [[int(x) for x in input().split()] for _ in range(N)]

def updateBoundary(x, y, d1, d2, boundary, N):

    tmp_y1, tmp_y2, tmp_y3, tmp_y4 = y, y, y-d1+1, y+d2-1
    
    # 5구역 경계 표시
    for tmp_x in range(x, x+d1+d2+1):
        if tmp_x <= x+d1:
            if (y-d1) <= tmp_y1 <= y: boundary[tmp_x][tmp_y1] = 5
            tmp_y1 -= 1
        else:
            if (y-d1) <=tmp_y3 <= (y-d1+d2): boundary[tmp_x][tmp_y3] = 5
            tmp_y3 += 1

        if tmp_x <= x+d2:
            if y <= tmp_y2 <= (y+d2): boundary[tmp_x][tmp_y2] = 5
            tmp_y2 += 1
        else:
            if (y-d1+d2) <= tmp_y4 <= (y+d2): boundary[tmp_x][tmp_y4] = 5
            tmp_y4 -= 1

    # 5구역 나누기
    for i in range(N):
        if boundary[i].count(5) == 1: continue

        is_5 = False
        for j in range(N):
            if boundary[i][j] == 5:
                if is_5 == False: is_5 = True
                else: is_5 = False
            elif is_5: boundary[i][j] = 5

    # 1, 2, 3, 4 구역 나누기
    for i in range(N):
        for j in range(N):
            if boundary[i][j] != 5:
                if i < x+d1 and j <= y: boundary[i][j] = 1
                elif i <= x+d2 and y < j: boundary[i][j] = 2
                elif x+d1 <= i and j < y-d1+d2: boundary[i][j] = 3
                elif x+d2 < i and y-d1+d2 <= j: boundary[i][j] = 4


    return boundary

def getValue(maps, boundary, key, N):
    total = 0
    for i in range(N):
        for j in range(N):
            if boundary[i][j] == key:
                total += maps[i][j]
    return total



infos = []
for x in range(1, N):
    for y in range(1, N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if 1 <= x < x+d1+d2 <= N  and 1 <= y-d1 < y < y+d2 <= N:
                    infos.append((x, y, d1, d2))


population = 1e9
for x, y, d1, d2 in infos:
    boundary = [[0 for _ in range(N)] for _ in range(N)]
    boundary = updateBoundary(x-1, y-1, d1, d2, boundary, N)

    # 인구가 가장 많은 선거구와 가장 적은 선거구의 인구 차이의 최솟값 구하기
    min_population, max_population = 1e9, 0
    for k in range(1,6):
        total = getValue(maps, boundary, k, N)
        min_population = min(min_population, total)
        max_population = max(max_population, total)

    population = min(population, (max_population - min_population))
    
print(population)
