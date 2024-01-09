# 시작시간 기준정렬 -> o(nlogn)
# 1(1) 2(2)  3(3)  5(3)  6(1)  8(2)
# 3 * 5 * 1 + 2 * 1 * 3 + 1 * 2 * 5
# 혹시 누적합??
# 1 1 2 2 1 2

# 시간 차 배열을 있으면 1대 2대 3대 2대 1대
# -> 시간 차 배열 값 * cost 값으로
# 1 * 5 + 1 * 6+ 2 * 3 + 1 * 6 + 2 * 5

# 시간 간격 누적합 배열 갖도록 세팅

# 근데 맞왜틀

cost = list(map(int, input().split()))
cost[1] *= 2 # 2대당 가격 -> *2
cost[2] *= 3 # 3대당 가격 -> *3

time = []

for i in range(3) :
    start, end = map(int, input().split())
    time.append(start)
    time.append(end)

time.sort()
sum_time = []
for i in range(1, 6) :
    sum_time.append(time[i] - time[i - 1])

ans = 0
c_idx = 0
# print(cost)
# print(sum_time)

for i, num in enumerate(sum_time) :
    if i == 3 :
        c_idx = 1

    elif i == 4 :
        c_idx = 0

    else :
        c_idx = i

    ans += cost[c_idx] * num

print(ans)

# 15 25 30  50  70  80

# 10 5 20 20 10
#