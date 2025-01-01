# 10^4 * 10^6
# 어림도 없

# dp일 것 같?
# 중복되는 하위문제도 보이지 않는다

# 그러면 이분?
k, n = map(int, input().split())

k_li = []
answer = 0

for i in range(k) :
    num = int(input())
    k_li.append(num)
    answer = max(answer, num)

start = 0
end = answer

while start <= end :
    mid = (start + end) // 2
    answer = mid

    total_wire = 0

    for item in k_li :
        total_wire += item // mid

    if total_wire < n : # mid 값을 더 작아지게 해야함
        end = mid

    elif total_wire > n :
        start = mid + 1

    else :
        break

print(answer)



