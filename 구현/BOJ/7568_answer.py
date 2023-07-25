# 브루트포스
# https://claude-u.tistory.com/122
# 단순하게 이중 for문을 돌면서, 자신보다 키랑 몸무게가 큰 사람의 명수를 세서 자기 등수를 정하기만 하면 된다.
# 단순하게 모든 요소들을 탐색하는 방법도 고려해보자.

N = int(input())

l = []

for i in range(N) :
    w, h = map(int, input().split())
    l.append((w, h))

for i in l :
    rank = 1
    for j in l :
        if i[0] < j[0] and i[1] < j[1] :
            rank += 1
    print(rank, end = " ")