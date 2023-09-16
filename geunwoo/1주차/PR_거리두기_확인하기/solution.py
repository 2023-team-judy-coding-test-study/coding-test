from typing import *
from collections import deque

PLACE_SIZE = 5
dy = [0,0,-1,1]
dx = [-1,1,0,0]


class Node:
    def __init__(self, y, x, level):
        self.y = y
        self.x = x
        self.level = level

        
def solution(places: List[List[str]]):
    place_board_list = []
    for place in places:
        place_board = []
        
        for row in place:
            place_board.append(list(row))
            
        place_board_list.append(place_board)
    
    answer = []
    for place_board in place_board_list:
        if _is_safe_place(place_board):
            answer.append(1)
        else:
            answer.append(0)
    
    return answer


def _is_safe_place(place: List[List[str]]):
    global PLACE_SIZE
    for i in range(PLACE_SIZE):
        for j in range(PLACE_SIZE):
            if place[i][j] == "P":
                result = bfs(Node(i, j, 0), place)
                
                if result is False:
                    return False
    
    
    return True
                    

def bfs(node: Node, place: List[List[str]]):
    global PLACE_SIZE, dy, dx
    visited = [[0 for _ in range(PLACE_SIZE)] for _ in range(PLACE_SIZE)]
    q = deque()
    
    visited[node.y][node.x] = 1
    q.append(node)
    
    while q:
        now = q.popleft()
        
        if now.level >= 3:
            return True
        
        for i in range(4):
            ny = now.y + dy[i]
            nx = now.x + dx[i]
            
            if ny < 0 or nx < 0 or ny >= PLACE_SIZE or nx >= PLACE_SIZE:
                continue
            
            if visited[ny][nx] == 1:
                continue
                
            if place[ny][nx] == "X":
                continue
                
            if place[ny][nx] == "P":
                if now.level <= 1:
                    return False
            
            visited[ny][nx] = 1
            q.append(Node(ny, nx, now.level + 1))
            