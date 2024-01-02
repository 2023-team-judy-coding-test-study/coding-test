def solution(msg):
    answer = []

    tmp = ""
    index = 0
    pos = 27

    LZW_dict = {chr(65 + i): i + 1 for i in range(26)}

    while index < len(msg):
        tmp += msg[index]
        if tmp in LZW_dict:
            index += 1
        else:
            answer.append(LZW_dict[tmp[:-1]])
            LZW_dict[tmp] = pos
            pos += 1
            tmp = ""

    if tmp:
        answer.append(LZW_dict[tmp])

    return answer


print(solution("KAKAO"))
