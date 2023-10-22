def solution(m, n, board):
    board = [[c for c in s] for s in board]
    rectDirs = [(-1,0),(0,-1),(-1,-1)]
    
    def getRect(x,y):
        c = board[y][x]
        if c == ' ':
            return False
        posSet = {(x,y)}
        for xdir, ydir in rectDirs:
            newX, newY = x+xdir, y+ydir
            if c != board[newY][newX]:
                return False
            posSet.add((newX, newY))
        return posSet
    
    def fallBlock():
        for x in range(n):
            for y in range(m-2,-1,-1):
                c = board[y][x]
                if c == ' ':
                    continue
                newY = y
                for i in range(y+1,m):
                    if board[i][x] != ' ':
                        break
                    newY = i
                board[y][x] = ' '
                board[newY][x] = c
    
    answer = 0
    
    while True:
        rectSet = set()
        for y in range(1,m):
            for x in range(1,n):
                temp = getRect(x,y)
                if temp:
                    rectSet = rectSet | temp
        if len(rectSet) == 0:
            break
        for newX, newY in rectSet:
            answer += 1
            board[newY][newX] = ' '
        fallBlock()
            
    return answer