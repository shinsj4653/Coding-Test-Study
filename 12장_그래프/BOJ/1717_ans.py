# https://deep-learning-study.tistory.com/591

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

parent = [0] * (N + 1) # 부모 테이블 생성
for i in range(N + 1) : # 자기 자신을 부모로 설정
    parent[i] = i

# 루트 노트 찾는 함수
def find(a) :
    if a == parent[a] :
        return a
    p = find(parent[a])
    parent[a] = p
    return parent[a]

def union(a, b) :
    a = find(a)
    b = find(b)

    if a == b :
        return

    if a < b :
        parent[b] = a

    else :
        parent[a] = b

for _ in range(M) :
    o, a, b = map(int, input().split())
    if o == 0 :
        union(a, b)

    elif o == 1 :
        if find(a) == find(b) :
            print('YES')

        else:
            print('NO')