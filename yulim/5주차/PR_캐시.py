def solution(cacheSize, cities):
    answer = 0  # 실행 시간

    cities = [c.lower() for c in cities]
    cache = []

    if cacheSize == 0:
        return 5 * len(cities)

    for city in cities:
        if city in cache:
            answer += 1
            cache.append(cache.pop(cache.index(city)))
        else:
            answer += 5
            if len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(city)

    return answer


print(
    solution(
        3,
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
        ],
    )
)

print(
    solution(
        3,
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "Jeju",
            "Pangyo",
            "Seoul",
            "Jeju",
            "Pangyo",
            "Seoul",
        ],
    )
)

print(
    solution(
        2,
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
            "SanFrancisco",
            "Seoul",
            "Rome",
            "Paris",
            "Jeju",
            "NewYork",
            "Rome",
        ],
    )
)
print(
    solution(
        5,
        [
            "Jeju",
            "Pangyo",
            "Seoul",
            "NewYork",
            "LA",
            "SanFrancisco",
            "Seoul",
            "Rome",
            "Paris",
            "Jeju",
            "NewYork",
            "Rome",
        ],
    )
)
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))
