def solution(s):
    answer = len(s)

    for i in range(1, len(s) // 2 + 1):  # 압축 크기, 최대 압축 크기만큼 반복
        comp = ""  # 압축한 문자열
        prev = s[:i]  # 첫 데이터
        cnt = 1  # 반복 횟수

        for j in range(i, len(s) + 1, i):  # 두 번째 데이터 부터 마지막 까지
            if prev == s[j : j + i]:  # prev가 다음 데이터랑 같을 경우
                cnt += 1
            else:  # 다르면
                comp += str(cnt) + prev if cnt > 1 else prev  # 압축 문자열 생성
                prev = s[j : j + i]
                cnt = 1
        comp += str(cnt) + prev if cnt > 1 else prev
        answer = min(len(comp), answer)  # 더 짧으면 갱신

    return answer
