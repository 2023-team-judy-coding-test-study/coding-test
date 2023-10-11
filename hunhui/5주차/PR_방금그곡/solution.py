def calculateTime(start, end):
    sh, sm = map(int, start.split(':'))
    eh, em = map(int, end.split(':'))
    return (eh-sh)*60+em-sm

def makeMelody(melody):
    answer, i = '', 0
    while i < len(melody):
        m = melody[i:i+2]
        if len(m) == 2 and m[1] == '#':
            answer += m[0].lower()
            i += 1
        else:
            answer += m[0]
        i += 1
    return answer

def solution(m, musicinfos):
    m = makeMelody(m)
    answer = []
    for index, info in enumerate(musicinfos):
        start, end, title, melody = info.split(',')
        time = calculateTime(start,end)
        melody = makeMelody(melody)
        l = len(melody)
        melody = ''.join(melody[i%l] for i in range(time))
        if m in melody:
            answer.append((title, time))
    answer.sort(reverse=True, key=lambda x: x[1])
    return "(None)" if len(answer) == 0 else answer[0][0]