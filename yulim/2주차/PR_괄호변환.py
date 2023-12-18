def divide(s):
    open = 0
    close = 0
    for i in range(len(s)):
        if s[i] == '(':
            open += 1
        else:
            close += 1
        if open == close:
            return s[:i+1], s[i+1:]

def isRight(s): #올바른 문자열인지 확인
    open = 0
    for i in s:
        if open < 0:
            return False
        elif i == "(":
            open += 1
            continue
        open -= 1
    return True

def makeOpposite(s):
    ret = ""
    for i in s:
        if i == "(":
            ret += ")"
            continue
        ret += "("
    return ret


def solution(p):

    if isRight(p):
        return p
    
    u, v = divide(p)

    if isRight(u): # u가 올바른 문자열이면
        return u + solution(v)
    
    answer = "("
    answer += solution(v)
    answer += ")"
    answer += makeOpposite(u[1:-1])

    return answer

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))