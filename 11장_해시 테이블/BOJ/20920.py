# https://velog.io/@bjo6300/%EB%B0%B1%EC%A4%80-20920-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%98%81%EB%8B%A8%EC%96%B4-%EC%95%94%EA%B8%B0%EB%8A%94-%EA%B4%B4%EB%A1%9C%EC%9B%8C

# 사전식 정렬을 어떻게 해야하지??? -> 그냥 word 자체를 정렬하면 됨!
# 근데 시간초과..why?
# 1. 불필요한 for문 없애기
# sys.stdin.readline 으로 시간줄이기!

from collections import Counter
import sys
input = sys.stdin.readline

n, m = map(int, (input().rstrip().split()))
words = []

for i in range(n) :
    w = input().rstrip()
    if len(w) >= m :
        words.append(w)

counter = Counter(words)
# m_counter = counter.most_common()

# for value in m_counter :
#     ans.append((value[0], value[1], len(value[0])))

# ans.sort(key=lambda x:(-x[1], -x[2], x[0]))

# 위에 처럼 리스트를 따로 만들어서 튜플로 넣지 말고, counter 사전에서 items()와 sorted 함수 활용하여 list 화 시키기
# most_common 할 필요 없이, lambda 함수에서 정렬해도 된다.
# 이런식이면 for문 하나 줄이기 가능!
ans = sorted(counter.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))
#print(ans)

for a in ans:
    print(a[0])



