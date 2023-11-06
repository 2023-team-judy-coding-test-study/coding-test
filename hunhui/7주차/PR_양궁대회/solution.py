def solution(n, info):
    maxScore = 10
    apeachScore = sum([maxScore - i for i, count in enumerate(info) if count > 0])
    
    highScore = 0
    tempInfo = [0] * (maxScore + 1)
    answer = []
    
    def backtracking(leftCount, score):
        nonlocal highScore
        nonlocal answer
        
        if leftCount == 0:
            if highScore < score:
                answer = tempInfo[:]
                highScore = score
                return
            
            if highScore == score:
                if tempInfo[:] == answer:
                    return
                for i in range(maxScore,-1,-1):
                    cCount = answer[i]
                    myCount = tempInfo[i]
                    if cCount > myCount:
                        break
                    if myCount > cCount:
                        answer = tempInfo[:]
                        break
            return
        
        for i in range(maxScore + 1):
            if i == maxScore:
                tempInfo[maxScore] = leftCount
                backtracking(0, score)
                tempInfo[maxScore] = 0
            count = info[i] + 1
            if tempInfo[i] == 0 and leftCount >= count:
                tempInfo[i] = count
                backtracking(leftCount - count, score + (maxScore - i)*(2 if count > 1 else 1))
                tempInfo[i] = 0
        return
    
    backtracking(n, 0)
    
    if highScore <= apeachScore:
        return [-1]
        
    return answer