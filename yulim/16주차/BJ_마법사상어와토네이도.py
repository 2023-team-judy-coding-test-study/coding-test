from collections import deque

def bfs(x, y, d, N, board, visited):
    dv = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    sv = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-2,0), (0,2), (2,0), (0,-2)]
    # 1% -> 2% -> 5% -> 7% -> 10% -> a 순서
    sp = [1, 1, 2, 2, 5, 7, 7, 10, 10, 0]
    s = [[5, 3, 11, 9, 8, 6, 2, 7, 1, 0],
        [7, 5, 8, 10, 9, 0, 4, 1, 3, 2],
        [7, 1, 9, 11, 10, 6, 2, 5, 3, 4],
        [1, 3, 8, 10, 11, 0, 4, 7, 5, 6]]
    
    
    queue = deque([(x, y, d)])
    visited[x][y] = 1
    answer = 0
    while queue:
        x, y, d = queue.popleft()

        # 1. 시계 반대 방향으로 회전
        nd = (d + 3) % 4    

        # 2. 회전 한 방향으로 전진
        nx = x + dv[nd][0]
        ny = y + dv[nd][1]

        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            queue.append((nx, ny, nd))

        # 2-1. 회전 한 방향으로 전진할 수 없으면 기존 방향으로 전진
        elif nx < 0 or nx >= N or ny < 0 or ny >= N or visited[nx][ny] == 1:
                nx = x + dv[d][0]
                ny = y + dv[d][1]
                if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, d))
                    nd = d
                else:
                     continue
        

        # if board[nx][ny] == 0: continue

        # 3. 흩날리는 모래 계산
        per = board[nx][ny] / 100
        for idx, sd in enumerate(s[nd]):
            sx = nx + sv[sd][0]
            sy = ny + sv[sd][1]

            if 0 <= sx < N and 0 <= sy < N:
                if sp[idx] == 0: # 알파 자리라면
                    board[sx][sy] += board[nx][ny]
                    board[nx][ny] = 0
                    break
                
                board[sx][sy] += int(per * sp[idx])
                board[nx][ny] -= int(per * sp[idx])
                continue
            
            if sp[idx] == 0: # 알파 자리라면
                answer += board[nx][ny]
                board[nx][ny] = 0
                break

            answer += int(per * sp[idx])
            board[nx][ny] -= int(per * sp[idx])

    return answer

        


N = int(input())
board = [[int(x) for x in input().split()] for _ in range(N)]
visited = [[0] * N for _ in range(N)]



# 시작점, 시작 방향
x, y = N//2, N//2
d = 0
print(bfs(x, y, d, N, board, visited))
