# 모든 정점 탐색 -> 최악인 경우는 n ^ 2 -> 1억
# -> 1억이면 어? 틀린건가 한 번 생각해보고 들어가기
# -> 다른 알고리즘 있지 않을까하고 고민
# -> 만약 없다면 그냥 완전탐색 쓰기
# -> 근데 큰돌님 풀이랑 똑같
# dfs로 했을 때도 메모리 초과
# -> 예전에도 이런적 있어서 bfs로 풀었었다
# -> https://hstory0208.tistory.com/entry/Python%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%B0%B1%EC%A4%80-1325-%ED%9A%A8%EC%9C%A8%EC%A0%81%EC%9D%B8-%ED%95%B4%ED%82%B9
# 인터넷 풀이도 bfs로 해서 bfs로 짜봤다.

# 핵심 : 메모리 초과 났을 때, 기록용 자료구조를 dict가 아닌 array로 해보자

from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
relationship = [[] for _ in range(n + 1)]

# A가 B를 신뢰한다. (노드로 표현하면 B는 A의 부모이다.)
for _ in range(m):
    A, B = map(int, input().split())
    relationship[B].append(A)

def bfs(start):
    q = deque()
    q.append(start)
    cnt = 0

    visited = [False] * (n + 1)
    visited[start] = True

    while q:
        cur = q.popleft()
        for next in relationship[cur]:
            if not visited[next]:
                visited[next] = True
                q.append(next)
                cnt += 1
    return cnt


result = []
for start in range(1, len(relationship)):
    result.append(bfs(start))

for i in range(len(result)):
    if max(result) == result[i]:
        print(i + 1, end=" ")
