# 분명 내 풀이 맞는 것 같은데..흠
# 바킹독 영상 참고
# -> 범위를 벗어난 경우도 고려해야함 : -1 만 계속 해야 동생을 만남
# 따라서, 100000 * 2인 20만이 최대 범위
# -> 넘어간 경우, -1 만 계속 해야함 : 굉장히 불리
# https://wook-2124.tistory.com/273

import sys
from collections import deque

input = sys.stdin.readline

# n : 수빈, k : 동생
n, k = map(int, input().split())

MAX = 10 ** 5 # 시간초과 안나게 수 제한
dist = [0] * (MAX + 1)

def bfs() :
    q = deque()
    q.append(n)
    
    while q :
        x = q.popleft()
        if x == k :
            print(dist[x])
            break

        for nx in (x - 1, x + 1, x * 2) :
            if 0 <= nx <= MAX and not dist[nx] :
                dist[nx] = dist[x] + 1
                q.append(nx)

bfs()