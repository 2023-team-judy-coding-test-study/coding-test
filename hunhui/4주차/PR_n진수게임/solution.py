def baseConv(num, base):
    result, nums = '', '0123456789ABCDEF'
    while num:
        num, r = divmod(num, base)
        result = nums[r] + result
    return result if result != '' else '0'

def solution(n, t, m, p):
    answer, cNum, num, cCount, i = '', '0', 0, 0, 0
    while len(answer) < t:
        if i%m+1 == p:
            answer += cNum[cCount]
        i += 1
        cCount += 1
        if cCount == len(cNum):
            num += 1
            cNum = baseConv(num, n)
            cCount = 0
    return answer