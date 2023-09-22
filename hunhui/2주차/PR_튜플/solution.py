def solution(s):
    nums_strs = s[2:-2].split('},{')
    nums_list = [list(map(int, strs.split(','))) for strs in nums_strs]
    nums_list.sort(key=len)
    answer = []
    for nums in nums_list:
        for num in nums:
            if num not in answer:
                answer.append(num)
                break
    return answer