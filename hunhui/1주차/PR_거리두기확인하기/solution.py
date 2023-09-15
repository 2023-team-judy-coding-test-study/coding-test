x_len = 5
y_len = 5
    
def is_in_range(x, y):
    return x < x_len and x >= 0 and y < y_len and y >= 0

def is_near_p(place, dir_list):
    for i, d in enumerate(dir_list):
        x, y = d
        if not is_in_range(x, y):
            continue
        new_item = place[y][x]
        if new_item == 'P':
            return True
    return False
    
def make_pos_list(x, y, i = None):
    dir_list = [(x+1,y), (x,y+1), (x-1,y), (x,y-1)]
    if i == None:
        return dir_list
    return [d for idx, d in enumerate(dir_list) if (i+2) % 4 != idx]
            
    
def is_p_safe(place, x, y):
    dir_list = make_pos_list(x,y)
    for i, d in enumerate(dir_list):
        new_x, new_y = d
        if not is_in_range(new_x, new_y):
            continue
        new_item = place[new_y][new_x]
        if new_item == 'P':
            return False
        if new_item == 'O':
            new_dir_list = make_pos_list(new_x, new_y, i)
            if is_near_p(place, new_dir_list):
                return False
    return True
    
def is_place_safe(place):
    for y in range(0, y_len):
        for x in range(0, x_len):
            if place[y][x] == 'P' and not is_p_safe(place, x, y):
                return False
    return True

def solution(places):
    answer = []
    for place in places:
        if is_place_safe(place):
            answer.append(1)
        else:
            answer.append(0)
    return answer
