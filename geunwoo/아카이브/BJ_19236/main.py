import sys
input = sys.stdin.readline

from heapq import heapify, heappop, heappush
from collections import deque
from typing import *
from copy import deepcopy

class Node:
    def __init__(self, y, x, w):
        self.y = y
        self.x = x
        self.w = w

    def __lt__(self, o):
        return self.w < o.w
    
    def __repr__(self):
        return f"({self.y}, {self.x}, {self.w})"

#      ↑,  ↖, ←, ↙, ↓, ↘, →,  ↗
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, -1, -1, -1, 0, 1, 1, 1]

g_board = []
g_dir_board = []

result = 0


def main():
    global g_board, g_dir_board
    """
    7 6 2 3 15 6 9 8
    3 1 1 8 14 7 10 1
    6 1 13 6 4 3 11 4
    16 1 8 7 5 2 12 2
    """
    for _ in range(4):
        row = list(map(int, input().split()))
        
        g_board.append(row[::2])
        g_dir_board.append(list(map(lambda x: x-1,row[1::2])))
        
    
    dfs(g_board, g_dir_board, Node(0, 0, 0), 0)    
    print(result)
    

def move_all_fishes(board: List[list], dir_board: List[list], shark: Node):
    
    for i in range(1, 16 + 1):
        now: Optional[Node] = find_fish(board, i)
        
        if now is None:
            return
        
        direction = dir_board[now.y][now.x]
        for j in range(8):
            ny = now.y + dy[j]
            nx = now.x + dx[j]
            
            # 이동할 수 없을때 - 좌표를 벗어남
            if ny < 0 or nx < 0 or ny >= 4 or nx >= 4:
                direction = turn_left(direction)
                continue
            
            # 이동할 수 없을때 - 상어 만났을때
            if ny == shark.y and nx == shark.x:
                direction = turn_left(direction)
                continue
            
            dir_board[now.y][now.x] = direction
            
            board[shark.y][shark.x], board[ny][nx] = board[ny][nx], board[shark.y][shark.x]
            dir_board[shark.y][shark.x], dir_board[ny][nx] = dir_board[ny][nx], dir_board[shark.y][shark.x]
            break


def find_fish(board: List[list], idx: int):
    for i in range(4):
        for j in range(4):
            if board[i][j] == idx:
                return Node(i, j, board[i][j])
    
    return None
        
    
def turn_left(direction):
    return (direction + 1) % 8


def get_possible_pos(board: List[list], dir_board: List[list], shark: Node):
    positions = []
    direction = dir_board[shark.y][shark.x]
    
    for _ in range(4):
        ny = shark.y + dy[direction]
        nx = shark.x + dx[direction]
        
        if ny < 0 or nx < 0 or ny >= 4 or nx >= 4:
            continue
        
        if board[ny][nx] == -1:
            continue
        
        positions.append(Node(ny, nx, board[ny][nx]))
    
    return positions


def dfs(board: List[list], dir_board: List[list], shark: Node, total):
    global result
    
    board = deepcopy(board)
    dir_board = deepcopy(dir_board)
    
    total += board[shark.y][shark.x]
    board[shark.y][shark.x] = -1
    
    move_all_fishes(board, dir_board, shark)
    
    positions = get_possible_pos(board, dir_board, shark)
    
    if len(positions) == 0:
        result = max(result, total)
        return
    
    for pos in positions:
        dfs(board, dir_board, Node(pos.y, pos.x, pos.w), total)
    
if __name__ == '__main__':
    main()
    