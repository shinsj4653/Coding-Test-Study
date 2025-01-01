# https://deep-learning-study.tistory.com/604
# start, end를 index로 하는 이분 탐색이 아니라, 0 이랑 max(budget) -> 즉 값을 기준으로 이분탐색해나가면 된다.

import sys
input = sys.stdin.readline

n = int(input())
budget = list(map(int, input().split()))
m = int(input())

start, end = 0, max(budget)

# 이분탐색
while start <= end :
    mid = (start + end) // 2
    total = 0
    for b in budget :
        if b > mid :
            total += mid

        else :
            total += b
    if total <= m :
        start = mid + 1

    else :
        end = mid - 1
print(end)

