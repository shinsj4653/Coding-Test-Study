# 맞왜틀
# 인접행렬 써서 해결하는 거 아닌가?

# 정답
# 트리는 루트 노드부터 탐색하는 것이 쉽다!

# here 즉, 루트부터 탐색해서
# there로 탐색 -> 해당 로직은 here, 즉 root 는 탐색이 안됨
# -> root가 지워주는 경우를 따로 적어줘야 함

from collections import defaultdict
n = int(input())
parent = list(map(int, input().split()))
remove = int(input())

tree = defaultdict(list)
root = 0

def dfs(here) :
    ret = 0
    child = 0

    for there in tree[here] :
        if there == remove :
            continue

        ret += dfs(there)
        child += 1

    if child == 0 :
        return 1

    return ret


for i in range(n) :
    tree[i] = []
    if parent[i] == -1 :
        root = i
        continue

    else : # tree 노드
        tree[parent[i]].append(i)

if remove == root :
    print(0)

else :
    print(dfs(root))