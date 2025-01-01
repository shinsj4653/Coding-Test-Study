
import math
import sys, bisect
input = sys.stdin.readline

n = int(input())
budget = list(map(int, input().split()))
m = int(input())

if sum(budget) <= m :
    print(max(budget))

# 110 120 140 150 -> sum / 4 : 130
# 130 보다 큰 140 150 만 고려 -> len() -> 2, 남는 금액: 485 - 230 = 255
# 130 * 2 = 260 -> 줄이기 ->  130 - round((260 - 255) / 나머지len) => 127


# 시간 초과 남..-> 이분탐색 사용해보기로! -> sum // 4 값보다 큰 쪽만 고려하면됨
# else :
#     ans = sum(budget) // n
#     while True :
#         total = 0
#         for b in budget :
#             if b <= ans :
#                 total += b
#             else :
#                 total += ans
# 
#         if total <= m :
#             break
#         else :
#             ans -= 1
# 
#     print(ans)

else :
    middle = sum(budget) // n
    budget.sort()
    m_index = bisect.bisect_left(budget, middle)
    left = m - sum(budget[:m_index])
    tmp = m - middle

    if left >= middle * len(budget[m_index:]) :
        print(middle)

    else :
        print(math.floor(middle - math.ceil(middle * len(budget[m_index:]) - left) / len(budget[m_index:])))

