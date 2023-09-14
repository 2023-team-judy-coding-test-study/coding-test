from collections import deque
from math import floor, sqrt

def base_conversion(n, k):
    result = deque()
    while n > 0:
        result.appendleft(n%k)
        n //= k
    return ''.join(str(num) for num in result)

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, floor(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    nums = base_conversion(n, k).split('0')
    return len([1 for num in nums if num != '' and is_prime(int(num))])