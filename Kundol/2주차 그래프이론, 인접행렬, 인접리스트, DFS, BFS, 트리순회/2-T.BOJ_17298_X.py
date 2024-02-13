# n^2 불가능
# 반대로 탐색?
# 하나의 기록 배열
# 맨 오른쪽은 -1
# 그 다음 왼쪽요소와 현재 요소 비교
# 만약 현재가 크면 현재요소 기록
# 만약 왼쪽 요소가 더 크면 현재 max_num 바꾸고

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [-1 for _ in range(n)]
num = arr[n - 1] # 오큰수
prev = arr[n - 1] # 이전 수

for i in range(len(arr) - 2, -1, -1) :

    cur = arr[i]

    if cur > num :
        num = cur

    elif cur < num :
        if cur < prev:  # cur < prev
            # 오큰수를 이전 수로 업데이트
             num = prev
        dp[i] = num

    prev = cur

print(*dp)


