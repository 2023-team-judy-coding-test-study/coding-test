def solution(s):
    answer = []
    s = s[2:-2].split("},{")
    s.sort(key=len)
    
    for nums in s:
        num = nums.split(",")
        for n in num:
            if int(n) not in answer:
                answer.append(int(n))
    return answer

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))