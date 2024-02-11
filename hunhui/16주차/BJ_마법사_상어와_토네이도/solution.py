# 01:44
N = int(input())
sr = sc = N // 2
data = [list(map(int, input().split())) for _ in range(N)]

delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def rotate_90(proportion):
    return list(reversed(list(zip(*proportion))))

p = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], [0, 0, 0.02, 0, 0]]
p1 = rotate_90(p)
p2 = rotate_90(p1)
p3 = rotate_90(p2)
proportions = [p, p1, p2, p3]
alphas = [(2, 1), (3, 2), (2, 3), (1, 2)]

outer_sand = 0
tr = sr
tc = sc
curl = 0
turn = 2
now = 0
proportion = proportions[0]

while not (tr == 0 and tc == 0):
    tr += delta[curl][0]
    tc += delta[curl][1]
    now += 1
    sand = data[tr][tc]
    data[tr][tc] = 0
    left = sand

    for r in range(5):
        for c in range(5):
            now_sand = int(sand * proportion[r][c])
            left -= now_sand
            if 0 <= tr + r - 2 < N and 0 <= tc + c - 2 < N:
                data[tr + r - 2][tc + c - 2] += now_sand
            else:
                outer_sand += now_sand

    if 0 <= tr + alphas[curl][0] - 2 < N and 0 <= tc + alphas[curl][1] - 2 < N:
        data[tr + alphas[curl][0] - 2][tc + alphas[curl][1] - 2] += left
    else:
        outer_sand += left

    if now == turn // 2 or now == turn:
        curl = (curl + 1) % 4
        proportion = proportions[curl]
        if now == turn:
            now = 0
            turn += 2

print(outer_sand)