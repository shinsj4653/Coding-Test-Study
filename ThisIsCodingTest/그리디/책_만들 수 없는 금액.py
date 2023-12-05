# 9:59 ~ 10:15

# 만들 수 없는 양의 정수 금액 중 최솟값
# 조합??
# 만들 수 있는 가격 => 조합의 최솟값으로 세팅
# 비교하면서 만약 현재값 +1 한 거 보다 다음 조합 값이 클 경우, +1 한 값이 정답!

from itertools import combinations

N = int(input())
coins = list(map(int, input().split()))
price_set = set()

for n in range(1, N + 1) :
    for c in combinations(coins, n) :
        price_set.add(sum(c))

for i in range(1, max(price_set) + 1) :
    if i not in price_set :
        print(i)
        break

# 정답
# 정렬 기반 그리디
# 현재 상태를 1부터 target - 1 까지의 모든 금액을 만들 수 있는 상태라고 보자
# 이때 매번 target인 금액도 만들 수 있는지(현재 확인하는 동전의 단위가 target 이하인지) 체크하는 것
# 만약 해당 금액을 만들 수 있다면, target의 값을 증가(현재 상태를 업데이트)

n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data :
    # 만들 수 없는 금액을 찾았을 때, 반복 종료
    if target < x :
        break
    target += x

# 만들 수 없는 금액 출력
print(target)