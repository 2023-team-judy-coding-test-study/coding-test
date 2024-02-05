import sys
input = sys.stdin.readline

n = 0
board = []
#     좌,우,상,하
dx = [0,0,-1,1]
dy = [-1,1,0,0]


class Node:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def valid_heart(node: Node):
    global n, board
    cnt = 0
    
    for i in range(4):
        nx = node.x + dx[i]
        ny = node.y + dy[i]
        
        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue
        
        if board[nx][ny] == 1:
            cnt += 1
        
    if cnt >= 4:
        return True

    return False

def count_physic_len(heart: Node, direct: int):
    cnt = 0
    node = heart
    
    while True:
        nx = node.x + dx[direct]
        ny = node.y + dy[direct]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            break
        
        if board[nx][ny] == 0:
            break
            
        node = Node(nx, ny)
        cnt += 1
    
    return cnt

def main():
    global n, board
    
    n = int(input())
    
    # init    
    for _ in range(n):
        row = list(map(lambda x: 1 if x == '*' else 0, list(input().strip())))
        
        board.append(row)
    
    # 심장 찾기
    heart = Node(0,0)
    already_find = False
    for i in range(n):
        if already_find is True:
            break
        
        for j in range(n):
            if board[i][j] == 1 and valid_heart(Node(i,j)) is True:
                heart = Node(i,j)
                already_find = True
                break
    
    result = []
    # 왼팔
    left_arm = count_physic_len(heart, 0)
    result.append(left_arm)
    
    # 오른팔
    right_arm = count_physic_len(heart, 1)
    result.append(right_arm)
    
    # 허리
    waist = count_physic_len(heart, 3)
    result.append(waist)
    
    # 왼다리
    left_leg = count_physic_len(Node(heart.x+waist, heart.y-1), 3)
    result.append(left_leg)
    
    # 오른다리
    right_leg = count_physic_len(Node(heart.x+waist, heart.y+1), 3)
    result.append(right_leg)
    
    print(heart.x+1, heart.y+1)
    print(*result)
    

if __name__ == '__main__':
    main()