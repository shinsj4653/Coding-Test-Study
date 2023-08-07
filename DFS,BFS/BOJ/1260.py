# 이 문제로 DFS, BFS 개념 마스터 하자

# dfs: https://data-marketing-bk.tistory.com/entry/DFS-%EC%99%84%EB%B2%BD-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC
# bfs: https://data-marketing-bk.tistory.com/entry/BFS-%EC%99%84%EB%B2%BD-%EA%B5%AC%ED%98%84%ED%95%98%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

from collections import deque, defaultdict

def dfs(graph, v, visited) :
    visited.append(v)
    print(v, end=" ")

    for node in graph[v] :
        if node not in visited :

            dfs(graph, node, visited)

def bfs(graph, v) :
    queue, visited = deque(), []
    queue.append(v)

    while queue :
        node = queue.popleft()
        if node not in visited :
            visited.append(node)
            print(node, end =" ")
            queue.extend(graph[node])

n, m, v = map(int, input().split())
graph = defaultdict(list)


for i in range(m) :
    n1, n2 = map(int, input().split())

    graph[n1].append(n2)
    graph[n2].append(n1)
    graph[n1].sort()
    graph[n2].sort()

dfs(graph, v, [])
print()

result = bfs(graph, v)







