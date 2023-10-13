"""
def solution(files):
    answer = []
    datas = []

    for file in files:
        head, number, tail = "", "", ""

        for i in range(len(file)):  # head 분리
            if file[i].isdigit():
                head = file[:i]
                number = file[i:]
                break

        for i in range(len(number)):  # number, tail 분리
            if not number[i].isdigit():
                tail = number[i:]
                number = number[:i]
                break

        datas.append([head, number, tail])

    datas = sorted(datas, key=lambda x: (x[0].lower(), int(x[1])))
    answer = ["".join(x) for x in datas]
    return answer
"""
##############
# 다른 사람 풀이 - 정규표현식 이용
# 파이썬이 stable sort를 지원해줘서 고려하지 않아도 됨
import re


def solution(files):
    temp = [re.split(r"([0-9]+)", s) for s in files]

    sort = sorted(temp, key=lambda x: (x[0].lower(), int(x[1])))

    return ["".join(s) for s in sort]


print(
    solution(
        ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
    )
)
