# 기존에 알고 있던 다익스트라랑 다른 것 같다
# 강의를 들으면서 개념을 다시 정리해보기로 함
# https://sungmin-joo.tistory.com/33

import sys, heapq
from collections import defaultdict

INF = int(1e9)

input = sys.stdin.readline

graph = defaultdict(list)

v, e = map(int, input().split())
start = int(input())

dist = [INF] * (v + 1)

for i in range(e) :
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dist[start] = 0

q = []
heapq.heappush(q, (0, start))

while q :
    time, node = heapq.heappop(q)

    if dist[node] < time :
        continue

    for next_node, w in graph[node] :
        alt = time + w
        if alt < dist[next_node] :
            dist[next_node] = alt
            heapq.heappush(q, (alt, next_node))

# print(dist)
for i in range(1, v + 1) :
    print("INF" if dist[i] == INF else dist[i])




