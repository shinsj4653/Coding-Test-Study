# 정답
# 가장 빠른 시간 -> bfs 떠올리기
# 방향이 4개인 탐색에서 3개로 바뀌었다.

# 너무 완탐이라고 "재귀로 풀어야지"를 악착같이 생각하지 말기
# bfs로 풀어보는 유연한 자세 가지기

# 반례 : 예시는 n, k 다른 경우
# -> 반대로 같은 경우를 생각해보기
# -> 또는 최소, 최대
# -> 또는 없거나, 있거나를 생각

# 코테에선 무조건 반례가 나옴

from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

if n == k:
    print(0)
    print(1)

else :
    MAX = 10 ** 5
    visited = [0 for _ in range(MAX + 1)]
    visited[n] = 1
    cnt = [0 for _ in range(MAX + 1)]
    cnt[n] = 1
    q = deque([n])

    while q :
        now = q.popleft()
        for next in [now + 1, now - 1, now * 2] :
            if 0 <= next <= MAX :
                if not visited[next] :
                    q.append(next)
                    visited[next] = visited[now] + 1
                    cnt[next] += cnt[now]

                elif visited[next] == visited[now] + 1 :
                    cnt[next] += cnt[now]

    print(visited[k] - 1)
    print(cnt[k])