def solution(s: str):
    set_str_list = s[2:-2].split("},{")
    set_list = []
    for set_str in set_str_list:
        set_list.append(set(map(int, set_str.split(","))))

    set_list.sort(key=lambda tuple: len(tuple))
    set_list_size = len(set_list)

    answer = list(set_list[0])
    if set_list_size == 1:
        return answer

    for i in range(1, set_list_size):
        prev_set = set_list[i-1]
        sub_set = set_list[i] - prev_set
        answer += list(sub_set)

    return answer
