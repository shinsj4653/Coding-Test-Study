import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temperature = list(map(int, input().split()))

start, end = 0, k
answer = sum(temperature[start:end])
cur_sum = answer

while end < n :
    cur_sum += temperature[end]
    cur_sum -= temperature[start]
    answer = max(answer, cur_sum)

    start += 1
    end += 1

print(answer)