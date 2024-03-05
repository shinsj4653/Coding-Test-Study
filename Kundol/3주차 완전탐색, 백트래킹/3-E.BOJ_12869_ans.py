# 공격 패턴을 경우의 수로 만들기
# -> 그러면 시간 줄이기 가능
# -> 일일히 permutation 안 만들어도됨

# 메모리 초과 -> bfs 고려
# 풀이 여러번 보면서 복습하기!
# dp 스럽게 생각하는 힘 기르기

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
scv = [0 for _ in range(3)]

for i in range(n) :
    scv[i] = a[i]

dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
v = [[[0 for _ in range(64)] for _ in range(64)] for _ in range(64)]
INF = 10e9

atk = [
    [9, 3, 1],
    [9, 1, 3],
    [3, 9, 1],
    [3, 1, 9],
    [1, 3, 9],
    [1, 9, 3]
]

def solve(a, b, c) :
    v[a][b][c] = 1
    q = deque([(a, b, c)])

    while q :
        num = q.popleft()
        a = num[0]
        b = num[1]
        c = num[2]

        if v[0][0][0] :
            break

        for i in range(6) :
            na = max(0, a - atk[i][0])
            nb = max(0, b - atk[i][1])
            nc = max(0, c - atk[i][2])

            if v[na][nb][nc] : continue
            v[na][nb][nc] = v[a][b][c] + 1
            q.append((na, nb, nc))

    return v[0][0][0] - 1

print(solve(scv[0], scv[1], scv[2]))



