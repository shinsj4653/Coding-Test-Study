# 그림으로 시간대 그리면 -> 특정 구간에 몇 대인지 구해야 한다는 것을 인식
# 도착한 시간대에 따라 cnt 배열
# 시각은 이상 미만이다

cost = list(map(int, input().split()))

time = [0] * 105

for i in range(3) :
    start, end = map(int, input().split())
    for j in range(start, end) :
        time[j] += 1

res = 0

for i in range(101) :
    if time[i] :
        if time[i] == 1 :
            res += 1 * cost[0]

        elif time[i] == 2 :
            res += 2 * cost[1]

        elif time[i] == 3:
            res += 3 * cost[2]

print(res)