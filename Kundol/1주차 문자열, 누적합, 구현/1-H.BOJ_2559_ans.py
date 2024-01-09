# 누적합
# 10^5가 최대라 o(n^2)은 불가능
# o(n)에 해결해야함

# 교안 다시 보며 복습!

# 맞왜틀..
# 분명 교안 보고 잘 푼 것 같은데..
# -> 마지막 load - load 누적합 끼리 계산할 때의 범위가 잘못되었음
# 한 칸 더 있다는 걸 항상 인지하기

n, k = map(int, input().split())
load = [0 for _ in range(n + 1)]
arr = list(map(int, input().split()))
ans = -100 * 100000
for i in range(1, len(arr) + 1) :
    load[i] = load[i - 1] + arr[i - 1]

#print(load)

#  3 -2 -4 -9  0
#0 3  1 -3 -12 -12

for i in range(k, n + 1) :
    ans = max(ans, load[i] - load[i - k])

print(ans)
