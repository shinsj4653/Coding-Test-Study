# 부분 수열 갯수를 어떻게 관리해야할지 모르겠음
# 총 sum을 상태 관리, 그리고 각 수를 더할지, 더하지 말지로 경우를 나눔
# 즉 "2개씩" 나눠서 재귀!

import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))


cnt = 0

def func(cur, tot) :
    global cnt

    if cur == n :
        if tot == s :
            cnt += 1
        return

    func(cur + 1, tot)
    func(cur + 1, tot + arr[cur])

func(0, 0)
if s == 0:
    cnt -= 1

print(cnt)