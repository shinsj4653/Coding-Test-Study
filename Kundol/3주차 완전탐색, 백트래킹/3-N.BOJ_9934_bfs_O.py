# 현재 층, (왼쪽) (가운데 딱 하나) (오른쪽) -> 3개 재귀로 돌리기
# 메모리 초과 뜸
# bfs로 해야하나??

from collections import defaultdict, deque

k = int(input())
v = list(map(int, input().split()))

tree = defaultdict(list)
mid = len(v) // 2

q = deque([(v[mid:mid + 1], 0), (v[:mid], 1), (v[mid + 1:], 1)])


# 일부분 bfs, floodfill

# 3 164 527
# 6 1 4

while q:
    li, floor = q.popleft()

    if len(li) == 1:
        tree[floor].append(li[0])

    else :
        mid = len(li) // 2
        q.append((li[mid:mid + 1], floor))
        q.append((li[:mid], floor + 1))
        q.append((li[mid + 1:], floor + 1))

# print(tree)

for i in range(k + 1) :
    if len(tree[i]) > 0:
        print(*tree[i])

