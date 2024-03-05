# 정답
# 답은 왠지 idx 기반 bfs 로 해결할듯
# -> dfs로 해결

from collections import defaultdict

k = int(input())
v = list(map(int, input().split()))

end = pow(2, k) - 1
tree = defaultdict(list)

def go(s, e, level) :
    if s > e : return # 구간 쪼개기 문제에선 이러한 조건이 필수적!
    if s == e : # 숫자가 같을 때 -> tree에 넣어줘야할 때
        tree[level].append(v[s])
        return

    mid = (s + e) // 2
    tree[level].append(v[mid])
    go(s, mid - 1, level + 1)
    go(mid + 1, e, level + 1)

go(0, end, 1)