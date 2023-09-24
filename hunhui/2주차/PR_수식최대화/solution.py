from itertools import permutations
import re

def calc_op(n1,n2,op):
    if op == '*':
        return n1 * n2
    if op == '+':
        return n1 + n2
    if op == '-':
        return n1 - n2

def calc(e, ops):
    for op in ops:
        i = 0
        while i < len(e):
            if op != e[i]:
                i += 1
                continue
            e[i-1] = calc_op(e[i-1], e[i+1], op)
            e = e[:i] + e[i+2:]
    return abs(int(e[0]))

def solution(expression):
    # 모든 연산자 우선순위 순서 만들기
    ops_list = list(permutations('*+-',3))
    # 숫자, 연산자를 고르고 숫자는 int로 형변환
    elements = re.findall(r'\d+|[*+-]', expression)
    for i in range(0,len(elements),2):
        elements[i] = int(elements[i])
    # 각 요소들을 연산자 우선순위들로 계산한 값 중 최대값을 반환
    return max(calc(elements[:], ops) for ops in ops_list)