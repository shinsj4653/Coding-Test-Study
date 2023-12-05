# 10:15 ~ 10:30

# 서로 무게가 다른 볼링공
# => set() 으로 중복제거 후, 2개 조합 때리면 될듯
# 중복 제거 하면 안됨! 1,3,2,2 면 1,2 가 2번 세져야 해서
# => 2개짜리 조합 중, 서로 다른 경우에만 result + 1 하면 될듯

from itertools import combinations

n, m = map(int, input().split())
balls = list(map(int, input().split()))

result = 0

for c in combinations(balls, 2) :
    if c[0] != c[1] :
        result += 1

print(result)

# 정답
# "무게" 마다 볼링공이 몇 개 있는지 계산!
# A가 특정한 무게의 볼링공 선택했을 때, 이어서 B가 볼링공을 선택하는 경우를 차례대로 계산
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array = [0] * 11

for x in data :
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1) :
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수 제외)
    result += array[i] * n # B가 선택하는 경우의 수와 곱하기

print(result)