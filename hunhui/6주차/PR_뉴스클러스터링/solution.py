from math import floor
from collections import Counter

CONSTNUM = 65536

def strToCounter(s):
    temp, answer = '', []
    for c in s:
        if not c.isalpha():
            temp = ''
            continue
        temp += c.lower()
        if len(temp) == 2:
            answer.append(temp)
            temp = temp[1:]
    return Counter(answer)

def solution(str1, str2):
    cnt1, cnt2 = strToCounter(str1), strToCounter(str2)
    allKeys = set(list(cnt1.keys()) + list(cnt2.keys()))
    inter = 0
    union = 0
    for key in allKeys:
        if key in cnt1 and key in cnt2:
            inter += min(cnt1[key], cnt2[key])
        union += max(cnt1[key] if key in cnt1 else 0, cnt2[key] if key in cnt2 else 0)
    return CONSTNUM if union == 0 else floor(inter/union*CONSTNUM)