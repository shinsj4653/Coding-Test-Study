# sol1
# O(N^2)은 안됨
# 메모리는 256mb
# 최대 인원수

# 인원수 대로 정렬 필요?
# 회의 K는 K - 1과 K + 1과만 겹침

# ds: 회의 선택된 여부 기록하는 dict
# algo: 정렬, 탐색

# 시작 위치를 0부터, 1부터 둘다 하고 비교?
# 그래도 틀림

# https://yiseul-coding.tistory.com/36
# 정답 : dp

import sys
input = sys.stdin.readline

n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]

# 시작 시간 기준으로 오름차순 정렬
array.sort()

dp = [0] * n
dp[0] = array[0][2]

for i in range(1, n) :
    dp[i] = max(dp[i - 1], dp[i - 2] + array[i][2])

print(dp[n - 1])

