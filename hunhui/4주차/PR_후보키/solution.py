from itertools import combinations as comb

def solution(relation):
    # 컬럼 개수, 레코드 수
    colCount, rowCount = len(relation[0]), len(relation)
    # 후보키 집합
    cKeys = set()
    for i in range(colCount):
        # 튜플 조합 생성
        combs = comb(range(colCount),i+1)
        # 튜플 조합 중 후보키가 포함되는 조합 제거
        combs = [c for c in combs if all(not set(key).issubset(set(c)) for key in cKeys)]
        # 조합들을 반복을 돌며 각 조합이 후보키인지 체크
        for c in combs:
            checkSet = set()
            for row in relation:
                checkSet.add(tuple(row[i] for i in c))
            if len(checkSet) == rowCount:
                cKeys.add(c)
    # 후보키의 개수를 반환
    return len(cKeys)