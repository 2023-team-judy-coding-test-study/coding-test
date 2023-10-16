from typing import *
from collections import deque

import sys
input = sys.stdin.readline

dir_idx = 0
board: list

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def main():
    global dir_idx, board
    
    n = int(input())
    board = [[0 for _ in range(n)] for _ in range(n)]
    
    # 사과 위치: 2
    k = int(input())
    for _ in range(k):
        y, x = map(int, input().split())
        
        board[y-1][x-1] = 2        
        
    # 방향 정보 입력, X초 C방향
    l = int(input())
    dir_info_list: List[Node] = []
    for _ in range(l):
        x, c = input().split()
        x = int(x)
        
        dir_info_list.append([x, c])
    
    dir_dict = {}
    for info in dir_info_list:
        sec: int = info[0]
        dir: str = info[1]
        
        dir_dict[sec] = dir
        
    snake = deque()
    now = Node(0,0)
    snake.append(now)
    board[0][0] = 1
    cnt = 0
    while True:
        cnt += 1
        # 뱀 이동
        ny = now.y + dy[dir_idx]
        nx = now.x + dx[dir_idx]
        
        if ny < 0 or nx < 0 or ny >= n or nx >= n:
            break
        
        # 사과가 있다면,
        if board[ny][nx] == 2:
            board[ny][nx] = 1
            snake.append(Node(ny, nx))
            
            #방향 전환
            if cnt in dir_dict:
                if dir_dict[cnt] == "L":
                    dir_idx = dir_idx - 1 if dir_idx > 0 else 3
                else:
                    dir_idx = dir_idx + 1 if dir_idx < 3 else 0
        
        # 사과가 없다면,        
        elif board[ny][nx] == 0:
            board[ny][nx] = 1
            snake.append(Node(ny, nx))
            tail: Node = snake.popleft()
            board[tail.y][tail.x] = 0
            
            #방향 전환
            if cnt in dir_dict:
                if dir_dict[cnt] == "L":
                    dir_idx = dir_idx - 1 if dir_idx > 0 else 3
                else:
                    dir_idx = dir_idx + 1 if dir_idx < 3 else 0
        
        # 뱀 몸통을 만난다면
        else:
            break
        
        now = Node(ny, nx)
                
    print(cnt)


class Node:
    def __init__(self, y, x):
        self.y = y
        self.x = x
    
    def __repr__(self):
        return f"({self.y}, {self.x})"

if __name__ == '__main__':
    main()
    