import math

from typing import *

def solution(n, k):
    """
    1. 진법 변환
    2. 조건 검색
    3. 소수 판별
    """
    # 1. 진법 변환 
    num_str: str = _convert_number(n, k)
    num_len = len(num_str)
    
    num_str_list: List[str] = num_str.split("0")
    
    # 2. 조건 검색
    cnt = 0
    for num in num_str_list:
        if not num:
            continue
            
        # 3. 소수 판별
        if _is_prime(int(num)):
            cnt += 1     
    
    return cnt

                    
def _convert_number(n: int, k: int) -> str:
    """
    정수 n을 k 진법으로 변환하는 함수
    """
    number = ""
    while n > 0:
        remainder = n%k
        
        number += str(remainder)
        
        n = int(n/k)
    
    number = number[::-1]
    if number[0] == "0":
        number = number[1:]
    
    return number
        
        
def _is_prime(num: int) -> bool:
    """
    소수를 판별하는 함수
    """
    if num < 2:
        return False
    
    if num == 2:
        return True
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num%i == 0:
            return False
        
    return True
        
    