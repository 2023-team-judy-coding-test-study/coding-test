def dfs(tmp, depth, cur): 
    if depth == length:
        tmp = ''.join(sorted(tmp))
        menu[tmp] = menu.get(tmp, 0) + 1
        return
    
    for i in range(cur, len(order)):
        tmp[depth] = order[i]
        dfs(tmp, depth+1, i+1)
    

def solution(orders, course):
    global menu #카운팅 할 딕셔너리 - k,v
    global order
    global length
    answer = []
    menu = {}
    for order in orders:
        for length in course:
            tmp = [0] * length # node
            dfs(tmp, 0, 0)

    result = [0]*(max(course)+1)

    for k, v in menu.items():
        if len(k) in course:
            if v >= 2 and v >= result[len(k)]:
                result[len(k)] = v
    
    for length in course:
        for k, v in menu.items():
            if len(k) == length and v == result[length]:
                answer.append(k)

    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))