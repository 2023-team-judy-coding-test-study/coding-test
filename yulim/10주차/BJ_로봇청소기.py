from collections import deque

# 로봇 청소기가 바라보는 방향 d
# 0인 경우 북쪽 
# 1인 경우 동쪽 
# 2인 경우 남쪽 
# 3인 경우 서쪽

N, M = map(int, input().split())
r, c, d = map(int, input().split())
maps = [ [ int(x) for x in input().split()] for _ in range(N) ]

dv = [(-1, 0), (0,1), (1, 0), (0,-1)] # 방향 이동 벡터

def bfs(x, y, d):

    cnt = 1
    maps[x][y] = 2

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        is_in = False

        for _ in range(4): 
            d = (d + 3) % 4     # 반시계 방향으로 네 방향 검사
            nx = x + dv[d][0]
            ny = y + dv[d][1]

            if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 0:
                maps[nx][ny] = 2
                queue.append((nx,ny))
                cnt += 1
                is_in = True
                break


        if is_in == False: # 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
            # 후진
            tmp_x = x - dv[d][0]
            tmp_y = y - dv[d][1]
            
            # 벽이나 범위 내가 아니면 종료
            if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= M or maps[tmp_x][tmp_y] == 1:
                return cnt
            
            # 후진 가능하면 반복
            queue.append((tmp_x, tmp_y))
    return cnt

print(bfs(r, c, d))