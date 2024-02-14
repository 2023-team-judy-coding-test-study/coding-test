import sys
input = sys.stdin.readline

edge_list = [[]
        , [2], [3], [4], [5], [6]           # 1 ~ 5
        , [7, 22], [8], [9], [10], [11]     # 6 ~10
        , [12, 28], [13], [14], [15], [16]      # 11~15
        , [17, 30], [18], [19], [20], [21]      # 16~20
        , [33], [23], [24], [25], [26]        # 21~25
        , [27], [21], [29], [25], [31]      # 26~30
        , [32], [25], [33]                  # 31~33
    ]
    
score_list = [0
    , 0, 2, 4, 6, 8           # 1 ~ 5
    , 10, 12, 14, 16, 18     # 6 ~10
    , 20, 22, 24, 26, 28      # 11~15
    , 30, 32, 34, 36, 38      # 16~20
    , 40, 13, 16, 19, 25        # 21~25
    , 30, 35, 22, 24, 28      # 26~30
    , 27, 26, 0                  # 31~33
]

dices = list(map(int, input().split()))
pieces = [1 for _ in range(4)]
answer = 0

def main():
    global score_list, dices, pieces, answer
    
    backtracking(0, 0)
    
    print(answer)
    
    
def backtracking(depth, result):
    global score_list, dices, pieces, answer
    
    if depth == 10:
        answer = max(answer, result)
        return
    
    for i in range(4):
        e = pieces[i]
        
        # 첫번째 이동
        if len(edge_list[e]) == 2:
            ne = edge_list[e][1]
        else:
            ne = edge_list[e][0]
        
        # 2번째 이동 ~ n번째 이동
        for _ in range(1, dices[depth]):
            ne = edge_list[ne][0]
        
        # 도착했거나 (아직 도착하지 않고 and 거기 말이 없다면)
        if ne == 33 or (ne < 33 and ne not in pieces):
            before = pieces[i] # 이전 말의 위치
            pieces[i] = ne     # 현재 말 위치
            
            backtracking(depth+1, result + score_list[ne])
            
            pieces[i] = before     # 말 위치 복원
        

if __name__ == "__main__":
    main()