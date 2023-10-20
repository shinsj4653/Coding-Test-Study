# 바킹독 다익스트라 -> pre 배열 활용하는거에서 영감 얻음!
# 바텀업 방식에서, 각 숫자가 어떤 숫자로 변하는지에 대한 정보만 있으면
# 그거에 따라 역 추적해서 경로 출력 하면됨

# 1 : 1
# 2 : 2 -> 1
# 3 : 3 -> 1

# 4 : 4 -> 2 -> 1
# 5 : 5 -> 4 -> 2 -> 1
# 6 : 6 -> 2 -> 1
# 7 : 7 -> 6 -> 2 -> 1
# 8 : 8 -> 4 -> 2 -> 1
# 9 : 9 -> 3 -> 1

# 10 : 10 -> 9 -> 3 -> 1
# 10 // 2 -> 5, 10 // 3 -> 3, 10 - 1 -> 9

# 탑 다운이 아니라, 바텀업으로 가야할듯??

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input().rstrip())

stack = []

dp = [0] * (n + 1) # 연산을 하는 횟수 저장 배열?

graph = defaultdict(int) # 경로 복원용 사전
graph[3] = 1
graph[2] = 1
graph[1] = 1

if n == 1:
    print(dp[n])
    print(graph[n])
    exit()

for i in range(2, n + 1) :
    cur = i

    if cur % 3 == 0 and dp[cur // 3] <= dp[cur - 1] :
        graph[cur] = cur // 3
        dp[cur] = dp[cur // 3] + 1

    elif cur % 2 == 0 and dp[cur // 2] <= dp[cur - 1] :
        graph[cur] = cur // 2
        dp[cur] = dp[cur // 2] + 1

    else :
        graph[cur] = cur - 1
        dp[cur] = dp[cur - 1] + 1

print(dp[n])

print(n, end=" ")
value = graph[n]

while True :
    if value == 1:
        print(value)
        break
    else :
        print(value, end=" ")
        value = graph[value]
