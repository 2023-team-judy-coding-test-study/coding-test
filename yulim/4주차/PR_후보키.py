from itertools import combinations


def solution(relation):
    row = len(relation)
    col = len(relation[0])

    # 모든 가능한 조합들
    combi = []
    for i in range(1, col + 1):
        combi.extend(combinations(range(col), i))

    unique = []
    for i in combi:
        tmp = [tuple([item[key] for key in i]) for item in relation]

        if len(set(tmp)) == row:  # 유일성 # 셋으로 중복 제거한 길이와 row의 길이가 같을 때(중복이 없다는 뜻)
            put = True

            for x in unique:
                if set(x).issubset(set(i)):  # 최소성 # x.issubset(y) # x가 y의 부분집합인가?
                    put = False
                    break

            if put:
                unique.append(i)

    return len(unique)


print(
    solution(
        [
            ["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"],
        ]
    )
)


# [ (0,) ] tmp: [('100',), ('200',), ('300',), ('400',), ('500',), ('600',)]
# [ (1,) ] tmp: [('ryan',), ('apeach',), ('tube',), ('con',), ('muzi',), ('apeach',)]
# [ (2,) ] tmp: [('music',), ('math',), ('computer',), ('computer',), ('music',), ('music',)]
# [ (3,) ] tmp: [('2',), ('2',), ('3',), ('4',), ('3',), ('2',)]
# [ (0, 1) ] tmp: [('100', 'ryan'), ('200', 'apeach'), ('300', 'tube'), ('400', 'con'), ('500', 'muzi'), ('600', 'apeach')]
# [ (0, 2) ] tmp: [('100', 'music'), ('200', 'math'), ('300', 'computer'), ('400', 'computer'), ('500', 'music'), ('600', 'music')]
# [ (0, 3) ] tmp: [('100', '2'), ('200', '2'), ('300', '3'), ('400', '4'), ('500', '3'), ('600', '2')]
# [ (1, 2) ] tmp: [('ryan', 'music'), ('apeach', 'math'), ('tube', 'computer'), ('con', 'computer'), ('muzi', 'music'), ('apeach', 'music')]
# [ (1, 3) ] tmp: [('ryan', '2'), ('apeach', '2'), ('tube', '3'), ('con', '4'), ('muzi', '3'), ('apeach', '2')]
# [ (2, 3) ] tmp: [('music', '2'), ('math', '2'), ('computer', '3'), ('computer', '4'), ('music', '3'), ('music', '2')]
# [ (0, 1, 2) ] tmp: [('100', 'ryan', 'music'), ('200', 'apeach', 'math'), ('300', 'tube', 'computer'), ('400', 'con', 'computer'), ('500', 'muzi', 'music'), ('600', 'apeach', 'music')]
# [ (0, 1, 3) ] tmp: [('100', 'ryan', '2'), ('200', 'apeach', '2'), ('300', 'tube', '3'), ('400', 'con', '4'), ('500', 'muzi', '3'), ('600', 'apeach', '2')]
# [ (0, 2, 3) ] tmp: [('100', 'music', '2'), ('200', 'math', '2'), ('300', 'computer', '3'), ('400', 'computer', '4'), ('500', 'music', '3'), ('600', 'music', '2')]
# [ (1, 2, 3) ] tmp: [('ryan', 'music', '2'), ('apeach', 'math', '2'), ('tube', 'computer', '3'), ('con', 'computer', '4'), ('muzi', 'music', '3'), ('apeach', 'music', '2')]
# [ (0, 1, 2, 3) ] tmp: [('100', 'ryan', 'music', '2'), ('200', 'apeach', 'math', '2'), ('300', 'tube', 'computer', '3'), ('400', 'con', 'computer', '4'), ('500', 'muzi', 'music', '3'), ('600', 'apeach', 'music', '2')]
