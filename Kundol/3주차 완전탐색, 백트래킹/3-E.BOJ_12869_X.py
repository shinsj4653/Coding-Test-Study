# 공격 횟수의 최솟값
# -> O(nlogn) 내림차순 정렬
# -> 9 3 1 공격

# nlogn * 100? -> 2초 이내는 가능할듯
# 정렬 x
# 모든 경우의 수 따져봐야할 듯

# 조합 돌려서 계속 재귀
# 그리고 가지치기

# 다 했는데도 시간 초과 혹은 메모리 초과

import sys
from itertools import permutations

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

n = int(input())
scv = list(map(int, input().split()))
atk = [9, 3, 1]

ret = 10e9

def dfs(scv, num) :

    global ret

    if num > ret : # 이미 최솟값 있는데 만약 그거보다 더 횟수 넘어가면 아예 볼 필요도 없음
        return

    if sum(scv) <= 0 :
        ret = min(ret, num)
        return

    for c in permutations(scv, n):

        for i in range(n) :
            scv[i] = c[i]
            scv[i] -= atk[i]

        dfs(scv, num + 1)

        # 다시 원복 필요
        # 다음 턴에 영향 가기 떄문
        for i in range(n):
            scv[i] += atk[i]

dfs(scv, 0)
print(ret)



