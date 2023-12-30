# 6:35
# s = 1, n = 0


def rotation(n, d):

    if d == -1: #반시계 방향으로 회전
        tmp_gear = gears[n][0]
        for i in range(7): gears[n][i] = gears[n][i+1]
        gears[n][7] = tmp_gear

    if d == 1: #시계 방향으로 회전
        tmp_gear = gears[n][7]
        for i in range(7, 0, -1): gears[n][i] = gears[n][i-1]
        gears[n][0] = tmp_gear

    return

def solution(n, d):

    rs = [(n,d)]

    rdir = -d
    for i in range(n, 0, -1):
        if gears[i][6] != gears[i-1][2]:
            rs.append((i-1, rdir))
            rdir = -rdir
            continue
        break
    
    rdir = -d
    for i in range(n, 3):
        if gears[i][2] != gears[i+1][6]:
            rs.append((i+1, rdir))
            rdir = -rdir
            continue
        break

    print(rs) ####

    for x, y in rs:
        rotation(x, y)

    for i in range(4): ####
        print(gears[i])
    
    # for i in range(n, 0, -1):
    #     if gears[i][6] != gears[i-1][2]:
    #         rotation(i-1, rdir)
    #         rdir = -rdir

    # for i in range(n, 3):
    #     if gears[i][2] != gears[i+1][6]:
    #         rotation(i+1, rdir)
    #         rdir = -rdir



gears = [[int(x) for x in input()] for _ in range(4)]
K = int(input()) # 회전 횟수
info = [tuple(map(int, input().split())) for _ in range(K)]

for n, d in info: solution(n-1, d)

answer = 0
for i in range(4):
    if gears[i][0] == 1:
        answer += 2**i



print(answer)


