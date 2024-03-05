# 정답
# 기존의 bfs에서 trace(추적) 기능 추가
# -> prev 배열 사용


from collections import deque
import sys

input = sys.stdin.readline

max_n = 200004
ret = 0
n, k = map(int, input().split())

if n == k:
    print(0)
    print(k)

else:
    visited = [0 for _ in range(max_n)]
    prev = [0 for _ in range(max_n)]

    visited[n] = 1
    q = deque([n])

    while q :
        here = q.popleft()

        if here == k :
            ret = visited[k]
            break

        for next in [here + 1, here - 1, here * 2] :
            if 0 <= next < max_n :
                if not visited[next] :
                    visited[next] = visited[here] + 1
                    prev[next] = here # 넘어갈떄 마다 배열에 담으면 됨
                    q.append(next)

    v = []
    i = k

    while True:
        if i == n:
            break

        v.append(i)
        i = prev[i]

    v.append(n)

    print(ret - 1)
    for num in reversed(v) :
        print(num, end= " ")

