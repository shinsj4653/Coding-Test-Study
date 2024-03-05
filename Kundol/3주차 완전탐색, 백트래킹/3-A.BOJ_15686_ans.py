# bfs 인 것 까지 생각했지만 구현방법이 잘못된 것 같다
# 거리값 변수가 자꾸 0으로 유지된다.
# 정답 코드의 구현 형태를 공부해야겠다

# 정답
# 정말 무식하게 치킨집 조합 구한다음, 각 집들과의 거리의 최솟값을 구해주면 된다.
# bfs로 굳이 안 풀어도 되는 문제!

# -> 문제 조건 보고 조합 공식 써서 알고리즘의 최대 횟수 구하기
# -> 1억 미만이면 무식하게 풀어볼까 라고 꼭 생각하기!

# 13CX * 100 이 최대

from itertools import combinations

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
chicken = []
home = []

for i in range(n) :
    for j in range(n) :
        if city[i][j] == 2 :
            chicken.append((i, j))

        if city[i][j] == 1 :
            home.append((i, j))
result = 1e9
for c in combinations(chicken, m) :
    ways = []
    ret = 0

    for h in home :
        hx, hy = h
        _min = 1e9
        for y, x in c:
            dist = abs(h[0] - y) + abs(h[1] - x)
            _min = min(_min, dist)

        ret += _min

    result = min(result, ret)

print(result)
