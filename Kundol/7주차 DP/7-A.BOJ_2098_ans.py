# print(16*16*16)

from collections import deque
import sys

input = sys.stdin.readline

MAX_N = 16
INF = 10e9

n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(1 << MAX_N)] for _ in range(MAX_N)]
# 4 -> 3
# 3 -> 1
# 1 -> 2
# 2 -> 4

def tsp(here, visited) :

    if visited == (1 << n) - 1 :
        return w[here][0] if w[here][0] else INF

    ret = dp[here][visited]

    if ret != -1 :
        return ret

    ret = INF

    for i in range(n) :
        if visited & (1 << i) : continue
        if w[here][i] == 0 : continue

        ret = min(ret, tsp(i, visited | (1 << i)) + w[here][i])

    return ret


print(tsp(0, 1))