import sys
input = sys.stdin.readline


n, m = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합
dp = [0] * (n + 1)

for i in range(n) :
    dp[i + 1] = dp[i] + arr[i]

#print(dp)
for i in range(m) :
    start, end = map(int, input().split())
    start -= 1

    print(dp[end] - dp[start])