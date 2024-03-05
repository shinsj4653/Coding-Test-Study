# 문제 이해가 안감
# 1 2

# 1 2

# 예제 보고 이해함 -> 1번 결과가1, 2번 결과가 2
# 1 (1 2)
# 2 (3 4)
# 3 (2 3)
# 4
# 5 (1 2) (4 5)

# 현재 (높이값, 세로선 위치)
# (1 1)
# (1 2)
# (2 2)
# (3 2)
# (3 3)
# (4 3)
# (5 3)

# 효율적으로 푸는 방법 떠오르지 않음..
# 우선 싹 다 돌리고 각각의 사다리가 어디로 도착하는지 체크

from collections import defaultdict

n, m, h = map(int, input().split())
ladder = defaultdict(list)
location = [0 for _ in range(n + 1)]
check = [0 for _ in range(n + 1)]

l_check = [0 for _ in range(11)]



for i in range(m) :
    height, l = map(int, input().split())
    ladder[height].append((l, l + 1))
    l_check[l] += 1

print(l_check)

# 맨 처음에 각 출발점들이 어디로 도착하는지 체크
for start in range(1, n + 1) :
    height = 1
    end = start

    while height <= m :
        for line in ladder[height] :
            if end == line[0] :
                end = line[1]

            elif end == line[1] :
                end = line[0]

        height += 1

    location[start] = end

    if start == end :
        check[start] = 1

#print(location)
#print(check)

# 사다리 1 2 와 1 2 둘다 있다면 상쇄가 된다
# 상쇄해서 하는 방법 말고는 떠오르지가 않는다
# 사다리 둘 수 있는 전체 경우를 뽑는 생각도 했지만,
# 만약 34 두면 45를 못 두기 때문에 그걸 캐치하는 방법도 모르곗..

odd_cnt = 0
isAble = True

for num in l_check :
    if num % 2 == 1 :
        odd_cnt += 1

    if odd_cnt > 3 :
        isAble = False
        break

print(odd_cnt) if isAble else print(-1)

