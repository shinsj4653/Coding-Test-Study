import sys
from collections import defaultdict, deque

answer = 0

input = sys.stdin.readline
graph = defaultdict(list)

n, m = map(int, input().rstrip().split())
for i in range(m) :
    u, v = map(int, input().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

# visited
v = [False] * (n + 1)
queue = deque()

def bfs(queue) :

    while queue :
        node = queue.popleft()

        if not v[node] :
            v[node] = True

            for n in graph[node] :
                queue.append(n)


for i in range(1, n + 1) :
    if not v[i] :
        queue.append(i)
        bfs(queue)
        answer += 1

print(answer)