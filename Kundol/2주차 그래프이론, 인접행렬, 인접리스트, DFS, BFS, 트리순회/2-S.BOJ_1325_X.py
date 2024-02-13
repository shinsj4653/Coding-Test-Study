# n * m = 10억 -> 대충 1초
#   5
#   위
# 4 <- 3 <- 1
#   위
#   2
# 1 해킹 : 4
# 2 해킹 : 4
# 3 해킹 : 3
# 4 해킹 : 1
# 5 해킹 : 1

# 방향 그래프
# 퍼져나간다 -> bfs

# 인접행렬 형태로 해서 그 안에서 bfs 돌리면 될듯
# 방문한 visited 배열 length 구하면 해킹한 컴퓨터 개수 된다

# 첫 시도 : 메모리초과 발생


from collections import defaultdict, deque
import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

n, m = map(int, input().split())
max_num = 0
num_dict = defaultdict(int)
graph = defaultdict(list)
visited = [0 for _ in range(n + 1)]

for i in range(m) :
    a, b = map(int, input().split())
    # b -> a
    graph[b].append(a)

for here in range(1, n + 1) :
    cnt = 0
    q = deque()
    q.append(here)

    for i in range(1, n + 1) :
        visited[i] = 0

    while q :
        num = q.popleft()
        visited[num] = 1

        for there in graph[num] :
            q.append(there)

    v_cnt = visited.count(1)
    num_dict[here] = v_cnt
    max_num = max(max_num, v_cnt)

for key in num_dict :
    if num_dict[key] == max_num :
        print(key, end=" ")
