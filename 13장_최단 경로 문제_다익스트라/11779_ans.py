# 경로 기록 -> 바킹독 : pre 배열 활용??
# https://velog.io/@yoopark/baekjoon-11779

import sys, heapq
from collections import defaultdict

input = sys.stdin.readline
INF = int(1e9)

n = int(input().rstrip())
m = int(input().rstrip())

graph = defaultdict(list)

for i in range(m) :
    u, v, w = map(int, input().rstrip().split())
    graph[u].append((v, w))

start, end = map(int, input().rstrip().split())

dist = [INF] * (n + 1)
pre = [0] * (n + 1)

queue = []
dist[start] = 0

heapq.heappush(queue, (0, start))

while queue :
    price, node = heapq.heappop(queue)

    if dist[node] < price :
        continue

    for next_node, new_price in graph[node] :
        alt = price + new_price
        if alt < dist[next_node] :
            dist[next_node] = alt
            # 갱신할 때 pre에 이전 node append?
            # 이전꺼 기억만 하면된다!
            pre[next_node] = node
            heapq.heappush(queue, (alt, next_node))

# print(pre)

path = [end]
now = end

while now != start :
    now = pre[now]
    path.append(now)


path.reverse()

print(dist[end])
print(len(path))
print(" ".join(map(str, path)))