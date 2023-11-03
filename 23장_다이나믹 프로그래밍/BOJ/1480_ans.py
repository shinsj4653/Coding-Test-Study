# 비트마스킹 활용 DP
# 모든 경우의 다 해봐야 한다.

import sys
input = sys.stdin.readline

n, m, c = map(int, input().split())
jewels = list(map(int, input().split()))

# 보석 갯수 : n, 가방의 개수 : m, 가방의 최대 한도 : c
# jewels : 보석의 무게

# 결국 다 돌면서 찾아봐야함 -> 비트마스킹!
# dp 배열 요소가 뭘 뜻하는지 알아야 한다

# 현재 보석 사용 상태가 gems 일때, ex) 100 이면 3번째 보석만 사용한 형태, 11001, 1, 4, 5 번째 보석 사용한 상태
# 현재 사용중인 가방의 위치가 bag_idx 일때,
# 현재 사용중인 가방의 용량이 current_capacity 만큼 남았을 때
# 담을 수 있는 최대의 보석 개수

dp = [[[0 for i in range(c + 1)] for j in range(m + 1)] for k in range(1 << 14)]

def solution(gems, bag_idx, current_capacity) :
    # 가방 다 썻거나, 보석 다 썻으면??
    if gems == ((1 << n) - 1) or bag_idx >= m :
        return 0

    if dp[gems][bag_idx][current_capacity] != 0 :
        return dp[gems][bag_idx][current_capacity]

    now_answer = 0

    # 모든 보석을 돌면서 하나씩 다 넣어본다.
    for i in range(n) :

        # 지금 쓸려는 보석이 이미 사용한 보석이면??
        if (gems & (1 << i)) != 0 or jewels[i] > c :
            continue

        # 지금 가방에 넣을 수 있으면?
        if current_capacity >= jewels[i] :
            now_answer = max(now_answer, solution(gems | (1 << i), bag_idx, current_capacity - jewels[i]) + 1)

        # 못 넣으면? 다음 가방으로
        else :
            now_answer = max(now_answer, solution(gems, bag_idx + 1, c))

    dp[gems][bag_idx][current_capacity] = now_answer
    return now_answer

print(solution(0, 0, c))