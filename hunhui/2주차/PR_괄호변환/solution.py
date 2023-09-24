def split_p(p):
    count = 0
    is_correct_p = p[0] == '('
    for i, c in enumerate(p):
        if c == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return p[:i+1], p[i+1:], is_correct_p

def reverse_p(p):
    answer = ''
    for c in p:
        if c == '(':
            answer += ')'
        else:
            answer += '('
    return answer

def dfs(p):
    if p == '':
        return ''
    u, v, is_correct_p = split_p(p)
    if not is_correct_p:
        return '(' + dfs(v) + ')' + reverse_p(u[1:-1])
    return u + dfs(v)
    
def solution(p):
    return dfs(p)