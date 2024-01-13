from collections import deque

N = int(input())    #보드 정보
board = [[0 for _ in range(N)] for _ in range(N)]

K = int(input())    #사과의 위치 보드에 업데이트
for i in range(K):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1 

L = int(input())    #이동 정보
move = {}
for i in range(L):
    time, direction = input().split()
    move[int(time)] = direction

#1(상), 2(우), 3(하), 0(좌), 리스트는 [오른쪽으로 회전, 왼쪽으로 회전, 전진하는 경우] 
d = {1:[(0, 1), (0, -1), (-1, 0)], 
     2:[(1, 0), (-1, 0), (0, 1)],
     3:[(0, -1), (0, 1), (1, 0)], 
     0:[(-1, 0), (1, 0), (0, -1)]}    

def bfs(x, y, dir, now_time):
    queue = deque()
    snake = deque()
    queue.append((x, y))
    snake.append((x, y))


    while queue:
        tmp_x, tmp_y = queue.popleft()
        if now_time in move.keys():         #회전할 타이밍 이라면
            if move[now_time] == "D":       #오른쪽으로 회전
                nx = tmp_x + d[dir][0][0]
                ny = tmp_y + d[dir][0][1]
                dir = (dir + 1) % 4
            else:                           #왼쪽으로 회전
                nx = tmp_x + d[dir][1][0]
                ny = tmp_y + d[dir][1][1]
                dir = (dir + 3) % 4
        else:                               #회전할 타이밍이 아니면 전진
            nx = tmp_x + d[dir][2][0]
            ny = tmp_y + d[dir][2][1]

        if nx < 0 or nx >= N or ny < 0 or ny >= N or (nx, ny) in snake: #만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다.
            return now_time + 1
        
        queue.append((nx, ny))
        snake.append((nx, ny))
        now_time += 1
        
        if board[nx][ny] == 1:    #만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
            board[nx][ny] = 0
        
        else:   #만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
            snake.popleft()

    return now_time + 1

print(bfs(0, 0, 2, 0))
