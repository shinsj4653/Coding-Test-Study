# https://www.acmicpc.net/problem/2309

# 키의 합이 100
# 누적합?
# 근데 그냥 무식하게 2중 for문 해도 되지 않나??
# 놉..7중 for문 해야한다..
from itertools import combinations

hts = []
for i in range(9) :
    hts.append(int(input()))

# 큰 거 부터 봐야, 만약 넘는 경우 바로 다음 꺼 부터 출력
# 일곱 난쟁이 찾을 수 없는 경우 없으니까, 만약 100 넘으면 바로 그 수 pass

# 조합으로 계산하면? -> 9*8*7*6*5*4*3 -> 2초안에 해결 가능

b = []

def combi(start, b) :
    if len(b) == 7 and sum(b) == 100 :
        b.sort()
        for num in b :
            print(num)
        return

    for i in range(start + 1, 9) :
        b.append(hts[i])
        combi(i, b)
        b.pop()

    return

combi(-1, b)
