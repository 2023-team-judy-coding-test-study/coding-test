# 10:30 ~ 12:02 (1'32")
import copy
N, M = map(int, input().split())

maps = [[int(x) for x in input().split()] for _ in range(N)]

houses = []
chickens = []

for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            houses.append((i+1, j+1))
        elif maps[i][j] == 2:
            chickens.append((i+1, j+1))



c = []
def getChickens(tmp_chickens, result_chickens):
    global M, c

    if len(result_chickens) == M:
        c.append(copy.deepcopy(result_chickens))
        return
    
    elif len(tmp_chickens) == 0: return
    
    tmp = copy.deepcopy(tmp_chickens)

    while tmp:
        r = copy.deepcopy(result_chickens)
        r.append(tmp.pop(0))
        getChickens(tmp, r)
        

getChickens(chickens, [])

answer = 1e9

for cc in c:
    total = 0
    for i, j in houses:
        min_distance = 1e9
        for x, y in cc:
            tmp_min_distance = (abs(i-x) + abs(j-y))
            min_distance = min(min_distance, tmp_min_distance)
        
        total += min_distance
    answer = min(answer, total)
    
print(answer)
