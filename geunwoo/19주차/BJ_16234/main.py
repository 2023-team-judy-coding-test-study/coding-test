import sys
from collections import deque

input = sys.stdin.readline
dy = [0,0,-1,1]
dx = [-1,1,0,0]

n = 0
l = 0
r = 0
board = []
visited = []
guild_list = []

class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x


def main(): 
    global n, l, r, board, visited, guild_list
    # init
    n, l, r = map(int, input().split())
    
    for _ in range(n):
        row = list(map(int, input().split()))
        
        board.append(row)
    
    
    # 인구이동
    cnt = 0
    while True:
        guild_list = []
        visited = [[0 for _ in range(n)] for _ in range(n)]
        
        find_guild_candidate()
        
        if not guild_list:
            break
        
        check_move: bool = move_humanity()

        if check_move is False:
            break
        
        cnt += 1

    print(cnt)

def find_guild_candidate():
    global n, l, r, board, visited, guild_list
    
    guild_num = 1
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            
            _bfs(Node(i, j), guild_num)
            
            guild_num += 1
            

def move_humanity():
    global n, l, r, board, visited, guild_list
    check_move = False
    
    for guild in guild_list:
        # 연합 총 인구 수, 연합 구성 나라 수 구하기
        total = 0
        countries = 0   
        for y, x in guild:
            total += board[y][x]
            countries += 1
            
        # 평균 구하기
        avg = int(total/countries)
        
        #인구 이동
        for y, x in guild:
            if board[y][x] != avg:
                board[y][x] = avg
                check_move = True

    return check_move
            
        
def _bfs(node: Node, guild_num: int):
    global n, l, r, board, visited, guild_list
    guild = [[node.y, node.x]]
    
    q = deque()
    
    visited[node.y][node.x] = guild_num
    q.append(node)
    
    while q:
        now: Node = q.popleft()
        
        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]
            
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            
            gap = abs(board[now.y][now.x] - board[ny][nx])
            if gap < l or gap > r:
                continue
            
            if visited[ny][nx]:
                continue
            
            visited[ny][nx] = guild_num
            q.append(Node(ny, nx))
            
            guild.append([ny,nx])
    
    if guild:
        guild_list.append(guild)

    
if __name__ == '__main__':
    main()