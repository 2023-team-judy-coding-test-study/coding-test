def calc(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    return a * b

def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]

    ex = []
    tmp = ''
    for e in expression:
        if e.isdigit() == False:
            ex.append(int(tmp))
            ex.append(e)
            tmp = ''
            continue
        tmp += e
    ex.append(int(tmp))

    answer = []
    for operation in operations:
        tmp = ex[:]
        p = 0
        while len(tmp) > 1:
            if operation[p] in tmp:
                idx = tmp.index(operation[p])
                tmp.insert(idx-1, calc(tmp[idx-1], tmp[idx+1], operation[p]))

                tmp.pop(idx)
                tmp.pop(idx)
                tmp.pop(idx)
            else:
                p += 1
        answer.append(abs(tmp[0]))

    return max(answer)

print(solution("100-200*300-500+20"))
print(solution("50*6-3*2"))