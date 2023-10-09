def compression(s, n):
    # 누적 글자 길이, 현재 압축 횟수, 현재 압축 문자열
    answer, count, cStr = 0, 0, s[0:n]
    for i in range(0,len(s),n):
        temp = s[i:i+n]
        # 현재 압축 중인 문자열과 같으면 카운트 증가
        if cStr == temp:
            count += 1
        else:
            # 누적 글자 길이 증가(글자 길이 + 숫자 길이)
            answer += len(str(count))+n if count != 1 else n
            # 현재 압축 문자열 초기화
            cStr = temp
            # 현재 압축 횟수 초기화
            count = 1
    # 남은 문자열 만큼 누적 글자 길이 증가
    return answer + (len(str(count)+cStr) if count != 1 else len(cStr))

def solution(s):
    # 모든 글자 길이 만큼 압축하며 최소 글자 길이 구해서 반환
    return min([compression(s, n) for n in range(1,len(s)//2+1)]+[len(s)])