# 원하는 요소의 index를 활용하자
# 정렬까지는 맞았다. 하지만, 해당하는 국가의 index를 찾아서 그 index를 기준으로 풀어야한다.
# https://kau-algorithm.tistory.com/666
# 금, 은, 동이 모두 같은 국가가 있어도 맨 앞의 요소만 고려하면 되고, 서로 같은 요소들을 지나치더라도
# 순위 숫자 자체는 계속 올라가는 거에 집중하면 된다.

# "정렬"과 "index"를 활용해보는 연습!


N, K = map(int, input().split())
place = 1

l = []

for i in range(N) :
    c, gold, silver, bronze = map(int, input().split())
    l.append((c, gold, silver, bronze))

l.sort(key=lambda x:(-x[1], -x[2], -x[3]))

for i in range(N) :
    if l[i][0] == K :
        index = i

for i in range(N) :
    if l[index][1:] == l[i][1:] :
        print(i + 1)
        break