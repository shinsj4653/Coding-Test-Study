# 빈도수 카운트 -> map
# 만약 횟수가 같다면 먼저 나온게 앞에

# n + for 횟수 in 1000
        # if 횟수 in counter > 0
        # for num in 수열
        # -> 수열에 있는 순서대로 num 출력
from collections import Counter

n, c = map(int, input().split())
s = list(map(int, input().split()))

counter = Counter(s)

l = []

# for c in counter :
for c in counter:
    l.append((c, counter[c]))

l.sort(key=lambda x:(-x[1]))

for ll in l :
    num, cnt = ll
    for i in range(cnt) :
        print(num, end=" ")

# for cnt in range(1, 1001) :
#     if cnt in counter.values() :





