def solution(records):
    answer = []
    users = {}

    for record in records:
        r = record.split(" ")
        if r[0] == "Enter" or r[0] == "Change":  # 이름이 바뀔 수 있으면
            users[r[1]] = r[2]

    for record in records:
        r = record.split(" ")
        if r[0] == "Enter":
            answer.append(users.get(r[1]) + "님이 들어왔습니다.")
        elif r[0] == "Leave":
            answer.append(users.get(r[1]) + "님이 나갔습니다.")

    return answer
