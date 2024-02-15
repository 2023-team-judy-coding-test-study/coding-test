
import sys
from collections import deque
input = sys.stdin.readline


"""
               [2]
               WWW            
               WWW
               WWW
          [3]  [0]  [4]  [5]
          GGG  RRR  BBB  OOO
          GGG  RRR  BBB  OOO
          GGG  RRR  BBB  OOO
               [1]
               YYY
               YYY
               YYY  
"""
cube = [[] for _ in range(6)]

def main():
    global cube
    
    for _ in range(int(input())):
        input()
        # init cube
        cube = [[] for _ in range(6)]
        for _ in range(3):
            cube[0].append(['r', 'r', 'r']);
            cube[1].append(['y', 'y', 'y']);
            cube[2].append(['w', 'w', 'w']);
            cube[3].append(['g', 'g', 'g']);
            cube[4].append(['b', 'b', 'b']);
            cube[5].append(['o', 'o', 'o']);
        
        # set rotate infomation
        q = deque(input().strip().split())
        while q:
            go(q.popleft())
        
        # output result
        print_result()

def go(rot_info):
    global cube
    direction, cnt = rot_info
    cnt = 1 if cnt == "+" else 3 # 시계방향 -> 1번 회전, 반시계방향 -> 시계방향 3번 회전
    
    for _ in range(cnt):
        move(direction)
    
def move(direction):
    global cube
    """
    U: 윗 면, D: 아랫 면, F: 앞 면, B: 뒷 면, L: 왼쪽 면, R: 오른쪽 면
    """
    if direction == 'U':
        temp = cube[0][0]
        cube[0][0] = cube[4][0]
        cube[4][0] = cube[5][0]
        cube[5][0] = cube[3][0]
        cube[3][0] = temp
        move_dimension(2)
    
    elif direction == 'D':
        temp = cube[0][2]
        cube[0][2] = cube[3][2]
        cube[3][2] = cube[5][2]
        cube[5][2] = cube[4][2]
        cube[4][2] = temp
        move_dimension(1)
    
    elif direction == 'F':
        temp = cube[2][2]
        cube[2][2] = [cube[3][2][2], cube[3][1][2], cube[3][0][2]]
        cube[3][0][2], cube[3][1][2], cube[3][2][2] = cube[1][0]
        cube[1][0] = [cube[4][2][0], cube[4][1][0], cube[4][0][0]]
        cube[4][0][0], cube[4][1][0], cube[4][2][0] = temp
        move_dimension(0)
    
    elif direction == 'B':
        temp = cube[2][0]
        cube[2][0] = [cube[4][0][2], cube[4][1][2], cube[4][2][2]]
        cube[4][2][2], cube[4][1][2], cube[4][0][2] = cube[1][2]
        cube[1][2] = [cube[3][0][0], cube[3][1][0], cube[3][2][0]]
        cube[3][2][0], cube[3][1][0], cube[3][0][0] = temp
        move_dimension(5)    
    
    elif direction == 'L':
        temp = [cube[0][0][0], cube[0][1][0], cube[0][2][0]]
        cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
        cube[2][0][0], cube[2][1][0], cube[2][2][0] = cube[5][2][2], cube[5][1][2], cube[5][0][2]
        cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[1][2][0], cube[1][1][0], cube[1][0][0]
        cube[1][0][0], cube[1][1][0], cube[1][2][0] = temp
        move_dimension(3)
        
    elif direction == 'R':
        temp = [cube[0][0][2], cube[0][1][2], cube[0][2][2]]
        cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
        cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
        cube[5][0][0], cube[5][1][0], cube[5][2][0] = cube[2][2][2], cube[2][1][2], cube[2][0][2]
        cube[2][0][2], cube[2][1][2], cube[2][2][2] = temp
        move_dimension(4)
        
    
def move_dimension(index):
    global cube
    for _ in range(2):
        temp = cube[index][0][0]
        cube[index][0][0] = cube[index][1][0]
        cube[index][1][0] = cube[index][2][0]
        cube[index][2][0] = cube[index][2][1]
        cube[index][2][1] = cube[index][2][2]
        cube[index][2][2] = cube[index][1][2]
        cube[index][1][2] = cube[index][0][2]
        cube[index][0][2] = cube[index][0][1]
        cube[index][0][1] = temp


def print_result():
    global cube
    for i in range(3):
        for j in range(3):
            print(cube[2][i][j], end="")
        print()

if __name__ == "__main__":
    main()