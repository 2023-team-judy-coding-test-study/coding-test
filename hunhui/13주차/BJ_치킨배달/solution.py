from itertools import combinations
import math
n, m = map(int, input().split())
city = []
chicken_houses = []
houses = []
for i in range(n):
  infos = list(map(int, input().split()))
  city.append(infos)
  for j, info in enumerate(infos):
    if info == 1:
      houses.append((i, j))
    elif info == 2:
      chicken_houses.append((i, j))

# 각 집에서 각 치킨집까지의 거리를 구한다.
chicken_graph = []
for hi, hj in houses:
  house_to_chicken = []
  for ci, cj in chicken_houses:
    house_to_chicken.append(abs(hi-ci)+abs(hj-cj))
  chicken_graph.append(house_to_chicken)

# 남길 치킨집 m개를 고른다.
combs = list(combinations(range(len(chicken_houses)), m))
answer = math.inf
# 치킨집 조합 별로 최소 치킨 거리를 구해서 그중 가장 작은 것을 답으로 설정
for comb in combs:
  total_val = 0
  house_indexes = []
  for h in range(len(houses)):
    min_val = math.inf
    for i in comb:
      min_val = min(min_val, chicken_graph[h][i])
    total_val += min_val
  answer = min(answer, total_val)
print(answer)