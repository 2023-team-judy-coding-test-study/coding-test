r, c, k = map(int, input().split())

matrix = [[int(x) for x in input().split()] for _ in range(3)]

def calculate(matrix, key):
    
    new_matrix, length = [], 0
    for row in matrix:
        num_count, new_row = [], []
        for num in set(row): # set으로 숫자 중복 제거
            if num == 0: continue
            cnt = row.count(num)
            num_count.append((num, cnt)) # 숫자와 갯수 추가

        num_count.sort(key=lambda x: (x[1], x[0]))

        new_row = [x for y in num_count for x in y]

        new_matrix.append(new_row)
        length = max(length, len(new_row)) # 가장 긴 길이로 업데이트

    # 0 추가
    for row in new_matrix: 
        row += [0] * (length-len(row))
        if len(row) > 100: row = row[:100]
    
    return list(zip(*new_matrix)) if key == "C" else new_matrix


r -= 1
c -= 1

time = 0
while True:
    if time > 100:
        time = -1
        break
    if  0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and matrix[r][c] == k: break
    
    if len(matrix) >= len(matrix[0]): # 행 > 열 비교
        matrix = calculate(matrix, "R")
    else:
        matrix = calculate(list(zip(*matrix)), "C")
    time += 1

print(time)