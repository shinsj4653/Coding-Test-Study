# 반복되는 규칙 => 수열 생각!

answer = 0

N, M, K = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
first = nums[N - 1]
second = nums[N - 2]

count = int(M / (K + 1)) * K
count += M % (K + 1)

result = 0
result += (count) * first
result += (M - count) * second

print(result)

