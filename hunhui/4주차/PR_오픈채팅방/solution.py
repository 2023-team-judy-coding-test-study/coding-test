def solution(record):
    nickDict, logs, answer = {}, [], []
    for r in record:
        info = r.split()
        act, uid = info[0], info[1]
        if act == 'Leave':
            logs.append((uid, False))
        else:
            nickDict[uid] = info[2]
            if act == 'Enter':
                logs.append((uid, True))
    for log in logs:
        uid, isEnter = log
        answer.append(f'{nickDict[uid]}님이 {"들어왔" if isEnter else "나갔"}습니다.')
    return answer
