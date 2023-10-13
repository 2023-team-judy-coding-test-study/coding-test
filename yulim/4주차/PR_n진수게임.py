def solution(n, t, m, p):
    answer = ""
    data = "-0"  # 0일때
    nums = "0123456789ABCDEF"

    for i in range(t * m):  # 구할 수 * 게임 참가 인원 = 최대로 필요한 수의 갯수
        tmp = ""
        s = i

        while s > 0:  # n진수로 변환
            s, mod = divmod(s, n)
            tmp += nums[mod]
        data += tmp[::-1]

    for i in range(p, t * m + 1, m):
        answer += data[i]

    return answer


print(solution(2, 4, 2, 1))
