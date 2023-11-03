import sys
from collections import deque, defaultdict

n, m = map(int, input().split())

adj = defaultdict(list)
deg = [0] * (n + 1)

queue = deque([])

for i in range(m) :
    a, b = map(int, input().split())
    adj[a].append(b)
    deg[b] += 1

for i in range(1, n + 1) :
    if deg[i] == 0 :
        queue.append(i)

while queue :
    node = queue.popleft()
    print(node, end=" ")
    for next in adj[node] :
        deg[next] -= 1
        if deg[next] == 0 :
            queue.append(next)
