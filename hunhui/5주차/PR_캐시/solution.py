from collections import deque

def solution(cacheSize, cities):
    que, time = deque(), 0
    for city in cities:
        city = city.lower()
        if city in que:
            que.remove(city)
            que.append(city)
            time += 1
            continue
        que.append(city)
        if len(que) > cacheSize:
            que.popleft()
        time += 5
    return time