# 설마 deque를 매 턴 마다 생성하는 것 때문에 메모리 초과?
# -> dfs로 해보겠다
# 아예 ide가 종료된다ㅋㅋ..
# 아예 다른 방법이 필요한 것 같다

from collections import defaultdict
import sys

sys.setrecursionlimit(100000)

n, m = map(int, input().split())
max_num = 0
num_dict = defaultdict(int)
graph = defaultdict(list)

def dfs(here, visited) :

    visited[here] = 1
    num = 1

    for there in graph[here] :
        if not visited[there] :
            num += dfs(here, visited)

    return num


for i in range(m) :
    a, b = map(int, input().split())
    # b -> a
    graph[b].append(a)


for here in range(1, n + 1) :
    cnt = 0
    visited = [0 for _ in range(n + 1)]

    v_cnt = dfs(here, visited)
    num_dict[here] = v_cnt
    max_num = max(max_num, v_cnt)

for key in num_dict :
    if num_dict[key] == max_num :
        print(key, end=" ")