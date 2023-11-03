import sys
from collections import defaultdict, deque

input = sys.stdin.readline
N, M = map(int, input().split())

graph = defaultdict(list)
real_graph = defaultdict(list)

deg = [0] * (N + 1)

queue = deque([])
result = []

for i in range(M) :
    # A -> B
    A, B = map(int, input().split())
    graph[B].append(A) # key의 부모가 value
    real_graph[A].append(B)

for i in range(1, N + 1) :
    deg[i] = len(graph[i])
    if deg[i] == 0 :
        queue.append(i)

while queue :
    node = queue.popleft()
    result.append(node)

    # 해당 node를
    for next in real_graph[node] :
        deg[next] -= 1

        if deg[next] == 0:
            queue.append(next)

print(*result)

