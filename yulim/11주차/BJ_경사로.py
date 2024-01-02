# 4:50 ~ 6:02 (1시간 12분..)

count = 0

def check(maps): 
    global count 

    for i in range(N):

        line = True
        for j in range(N-1):

            if line == False:
                break

            if maps[i][j] - maps[i][j+1] == 1:    # 현재 칸이 다음 칸 보다 1 높으면
                
                if visited[i][j+1] == 0: visited[i][j+1] = 1
                else: 
                    line = False
                    break

                tmp_j = j+1
                for k in range(L - 1):
                    tmp_j += 1
                    if 0 <= tmp_j < N and maps[i][j+1] == maps[i][tmp_j] and visited[i][tmp_j] == 0:
                        visited[i][tmp_j] = 1
                        continue
                    line = False
                    break

            elif maps[i][j] - maps[i][j+1] == -1:    # 현재 칸이 다음 칸 보다 1 낮으면

                if visited[i][j] == 0: visited[i][j] = 1
                else: 
                    line = False
                    break

                tmp_j = j
                visited[i][j] = 1
                for k in range(L - 1):
                    tmp_j -= 1
                    if 0 <= tmp_j < N and maps[i][j] == maps[i][tmp_j]and visited[i][tmp_j] == 0:
                        visited[i][tmp_j] = 1
                        continue
                    line = False
                    break

            elif abs(maps[i][j] - maps[i][j+1]) >= 2: line = False   # 현재 칸과 다음 칸이 2이상 차이나면

        if line == True:
            count += 1


N, L = map(int, input().split())

visited = [[0 for _ in range(N)] for _ in range(N)]
maps = [[int(x) for x in input().split()] for _ in range(N)]
check(maps)


visited = [[0 for _ in range(N)] for _ in range(N)]
rmaps = [[0 for _ in range(N)] for _ in range(N)] 
for i in range(N):  # 왼쪽으로 90도 회전
    for j in range(N):
        rmaps[i][j] = maps[j][N-(i+1)]
check(rmaps)


print(count)
