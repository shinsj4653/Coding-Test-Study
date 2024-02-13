# bfs로 삭제한다음, max len 에 해당하는 원소 개수 구하기?
# -> 부모 key, 자식 list 형태로 나타내기
# -> 인접 행렬
# 그 다음, 삭제할 노드 기준으로 bfs
# -> 탐색하면서 삭제

# 0 - 1 2
# 1 - 3 4
# 2 -
# 3 -
# 4 -

# 0 - 1 2
# 1 -
# 2 - 3 4
# 3 -
# 4 - 5 6
# 5 -
# 6 - 7 8
# 7 -
# 8 -

# 0
# 1 2

#   3 4
#     5 6
#      7 8
from collections import defaultdict, deque

n = int(input())
parent = list(map(int, input().split()))
remove = int(input())

tree = defaultdict(list)

for i in range(n) :
    tree[i] = []
    if parent[i] == -1 :
        continue

    else : # tree 노드
        tree[parent[i]].append(i)

#print(tree)
q = deque()
q.append(remove)

# 파이썬 key 삭제
# https://crazyj.tistory.com/225

# bfs 탐색하면서 삭제
while q :
    # print('q : ', q)
    node = q.popleft()

    for no in tree[node] :
        q.append(no)

    if node in tree :
        del tree[node]

# print(tree)

cnt = 0

for t in tree :
    if len(tree[t]) == 0:
        cnt += 1

print(cnt)
