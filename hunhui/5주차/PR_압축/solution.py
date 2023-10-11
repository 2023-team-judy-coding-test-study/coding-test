def makeDict():
    start, end, index, wordDict = ord('A'), ord('Z'), 1, {}
    for i in range(start, end+1):
        wordDict[chr(i)] = index
        index += 1
    return wordDict, index
        
def solution(msg):
    wordDict, index = makeDict()
    temp, answer = '', []
    for i, c in enumerate(msg):
        if temp + c in wordDict:
            temp += c
        else:
            answer.append(wordDict[temp])
            wordDict[temp+c] = index
            index += 1
            temp = c
    return answer + [wordDict[temp]]