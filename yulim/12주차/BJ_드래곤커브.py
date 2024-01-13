# 5:55~7:34 (1'39")

# x, y
directions = [(1, 0), (0,-1), (-1, 0), (0, 1)]

N = int(input())
curves = [[int(x) for x in input().split()] for _ in range(N)]

checks = [(1, 0), (1,-1), (0, -1)]


def sol(x, y, d, n):

    tmp_d = [d,]
    tmp_xy = [(x,y),]

    x += directions[d][0]
    y += directions[d][1]

    tmp_xy.append((x,y))


    for i in range(n): #세대만큼 반복

        nd = len(tmp_d)
        for i in range(nd-1, -1, -1):
            d = (tmp_d[i] + 1) % 4
            x += directions[d][0]
            y += directions[d][1]
            tmp_xy.append((x, y))
            tmp_d.append(d)
    return tmp_xy

def check(x, y):
    for ix, iy in checks:
        if (x+ix, y+iy) not in xy:
            return 0
    return 1


xy = []
for x, y, d, g in curves:
    xy.append(sol(x, y, d, g))

xy = [ x for y in xy for x in y ] # 2차원 리스트를 1차원으로
xy = set(xy)

count = 0
for x, y in xy:
    if check(x, y):
        count += 1

print(count)
