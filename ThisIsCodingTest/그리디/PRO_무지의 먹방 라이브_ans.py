# https://programmers.co.kr/learn/courses/30/lessons/42891

# 10:32 ~ 풀이시간초과
# 전 풀이
def solution(food_times, k):
    # 200000^2 -> 40000000000 -> 2중 for문 불가능!

    # 다음 위치가 0일 때의 처리 어떻게?
    # 0,1,2 -> 위치 인덱스 배열 가지고 있고, 만약 해당 위치 값이 0되면,
    # -> 인덱스 배열에서 뺴기??

    idx = 0

    idx_list = [i for i in range(len(food_times))]

    while k > 0:

        # print('before')
        # print(idx)
        # print(idx_list)
        # print(food_times)

        if len(idx_list) == 0:  # 다 먹었다면
            break

        if food_times[idx_list[idx]] > 0:
            food_times[idx_list[idx]] -= 1

            if food_times[idx_list[idx]] == 0:
                idx_list.remove(idx_list[idx])
                idx -= 1

        idx += 1
        idx %= len(idx_list)

        k -= 1

        # print('after')
        # print(idx)
        # print(idx_list)
        # print(food_times)

    if k > 0:  # k > 0 이면, 모든 음식 다 먹었다는 뜻
        return -1
    else:  # k == 0 이면, 아직 먹을 음식 남았다.
        return idx + 1

# 0 일때, "적용되어야 하는 인덱스들 리스트에서 삭제 함으로써, 해당 인덱스를 거치지 않도록" 하는 방법 사용
# 하지만, 시간초과에 테스트도 여러개 틀림..


# 정답
# 시간이 적게 걸리는 음식부터 확인하는 "탐욕적 접근방식"
# 모든 음식을 시간을 기준으로 정렬한 뒤, 시간이 적게 걸리는 음식부터 제거
# -> 우선순위 큐

# k초 동안의 스케쥴링으로 하나하나씩 체크하는 방식으로는 안됨!

import heapq

def solution(food_times, k) :
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k :
        return -1

    # 시간이 작은 음식부터 빼야하므로, 우선순위 큐 이용
    q = []
    for i in range(len(food_times)) :
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간

    length = len(food_times) # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식의 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k :
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x:x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]



