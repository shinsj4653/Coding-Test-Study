import sys, collections
from collections import defaultdict
# defaultdict : https://dongdongfather.tistory.com/6

# 사전 : 최대 value에 대한 key값 찾기
# https://106hht.tistory.com/64

t = int(input())

for i in range(t) :
    score = defaultdict(int)
    n = int(input())

    team = list(map(int, sys.stdin.readline().split(" ")))
    team_counter = collections.Counter(team)

    f_counter = dict(team_counter)
    five = defaultdict(int) # 5순위 사람의 점수

    s = 1
    for t in team :

        if team_counter[t] >= 6 :
            if f_counter[t] > 2:
                score[t] += s
            if f_counter[t] == 2 :
                five[t] = s

            f_counter[t] -= 1
            s += 1


    new_score = [k for k, v in score.items() if min(score.values()) == v]

    if len(new_score) == 1 :
        print(new_score[0])
    else :
        ans = 1000
        key = 0
        for n in new_score :
            if ans > five[n] :
                ans = five[n]
                key = n

        print(key)