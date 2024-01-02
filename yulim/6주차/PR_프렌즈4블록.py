def pop_block(board, i, j):
    board[i][j] = 0
    for ii in range(i, 0, -1):
        board[ii][j] = board[ii - 1][j]
    board[0][j] = 0
    return board


def solution(m, n, board):
    answer = 0
    board = [list(x) for x in board]
    while True:
        pos = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if (
                    board[i][j] == board[i][j + 1]
                    and board[i][j] == board[i + 1][j]
                    and board[i][j] == board[i + 1][j + 1]
                    and board[i][j] != 0
                ):
                    pos.add((i, j))
                    pos.add((i, j + 1))
                    pos.add((i + 1, j))
                    pos.add((i + 1, j + 1))

        if pos:
            p = sorted(pos, key=lambda x: x[0])
            for i, j in p:
                board = pop_block(board, i, j)
                answer += 1
        else:
            break
    return answer


print(solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"]))
