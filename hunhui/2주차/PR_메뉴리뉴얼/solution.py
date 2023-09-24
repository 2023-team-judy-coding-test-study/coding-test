from collections import Counter
from itertools import combinations as comb

MIN_COUNT = 2

# orders에서 num개로 만들수 있는 모든 조합 얻기
def get_order_combs(num, orders):
    result_list = []
    for order in orders:
        if len(order) < num:
            break
        result_list += [''.join(strs) for strs in comb(order, num)]
    return result_list

# orders로 만든 조합 중 가장 많은 조합들 얻기
def get_most_common_orders(order_combs):
    orders = []
    max_count = MIN_COUNT
    for k, v in Counter(order_combs).items():
        if v > max_count:
            max_count = v
            orders = [k]
        elif v == max_count:
            orders.append(k)
    return orders
        
def solution(orders, course):
    answer = []
    orders = [''.join(sorted(list(s))) for s in orders]
    orders.sort(key=len, reverse=True)
    # 코스 개수 별로 가능한 조합 중 가장 많은 조합을 answer에 담음
    for num in course:
        order_combs = get_order_combs(num, orders)
        if len(order_combs) == 0:
            continue
        answer += get_most_common_orders(order_combs)
    return sorted(answer)