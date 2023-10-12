from typing import *
from collections import OrderedDict

CACHE_HIT = 1
CACHE_MISS = 5


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return None

        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        self.cache[key] = value

        self.cache.move_to_end(key)

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


def solution(capacity: int, cities: List[str]):
    cache = LRUCache(capacity=capacity)
    run_time = 0

    for city in cities:
        city = city.lower()

        if cache.get(city) is None:  # cache miss
            run_time += CACHE_MISS

        else:  # cache hit
            run_time += CACHE_HIT

        cache.put(city, True)

    return run_time
