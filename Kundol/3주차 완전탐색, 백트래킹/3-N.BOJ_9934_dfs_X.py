# 앞의 부등호 문제랑 유사한듯

# LVR -> 중위 탐색
# 탐색 순서에서 트리 복원을 해야하는 문제

# 213

# 1643527
# 트리 사전
# 0
# 1
# 2*k - 1
# 1024

# 101
#      2120212
#         32123032123

# 4
# 0
# 0 0
# 0 0 0 0
# 0 0 0 0 0 0 0 0
#

# 현재 층, (왼쪽) (가운데 딱 하나) (오른쪽) -> 3개 재귀로 돌리기
# 메모리 초과 뜸
# bfs로 해야하나??

import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

k = int(input())
v = list(map(int, input().split()))

tree = defaultdict(list)
mid = len(v) // 2

def visit(li, floor) :
    if len(li) == 1:
        tree[floor].append(li[0])
        return

    mid = len(li) // 2
    visit(li[:mid], floor + 1)
    l = list()
    l.append(li[mid])
    visit(l, floor)
    visit(li[mid + 1:], floor + 1)

visit(v[:mid], 1)
li = list()
li.append(v[mid])
visit(li, 0)
visit(v[mid + 1:], 1)

print(tree)

for i in range(k + 1) :
    if len(tree[i]) > 0:
        for num in tree[i] :
            print(num, end=" ")

        print()
