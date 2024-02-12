"""
방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하는 프로그램을 작성하시오. 
단, 모든 간선의 가중치는 10 이하의 자연수이다.

첫째 줄에 정점의 개수 V와 간선의 개수 E가 주어진다. (1 ≤ V ≤ 20,000, 1 ≤ E ≤ 300,000)
모든 정점에는 1부터 V까지 번호가 매겨져 있다고 가정한다. 
둘째 줄에는 시작 정점의 번호 K(1 ≤ K ≤ V)가 주어진다. 
셋째 줄부터 E개의 줄에 걸쳐 각 간선을 나타내는 세 개의 정수 (u, v, w)가 순서대로 주어진다.

5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

0
2
3
7
INF
"""
import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize


#init
V, E = map(int, input().split())
K = int(input())

edge_list = [[] for _ in range(V+1)]
dist = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    
    edge_list[u].append([w, v])
    

heap = []
heapq.heappush(heap, [0, K])
dist[K] = 0

# dijkstra
while heap:
    ew, ev = heapq.heappop(heap)
    
    if dist[ev] != ew: continue
    
    for nw, nv in edge_list[ev]:
        if dist[nv] > ew + nw:
            dist[nv] = ew + nw
        
            heapq.heappush(heap, [ew + nw, nv])

# output
for i in range(1, V+1):
    if dist[i] == INF: print("INF")
    else: print(dist[i])


