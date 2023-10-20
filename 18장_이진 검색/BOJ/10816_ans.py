# pos 를 찾긴 찾는데, 같은 요소가 여러개 있어서 먼가 결과 이상함
# -> 같은 값 중, 아무 인덱스를 넘겨줌..
# 헉 깨달음
# 알고리즘 인터뷰 책에서 본 아이디어 -> bisect_left와 bisect_right를 둘 다 활용!

import sys, bisect
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().rstrip().split()))
cards.sort()

m = int(input())
m_list = list(map(int, input().rstrip().split()))

# 무한 루프 안 빠지도록 주의
# mid 세팅할 때, st랑 en의 차이가 1일 때 주의!
# -> st + en + 1 을 더 해줘야 할 수도 있음!
def lower_idx(target) :
    st = 0
    en = n # 맨 끝이 cards의 length 임에 주의!

    while st < en :
        mid = (st + en) //  2
        if cards[mid] >= target :
            en = mid

        else :
            st = mid + 1

    return st


def upper_idx(target):
    st = 0
    en = n  # 맨 끝이 cards의 length 임에 주의!

    while st < en:
        mid = (st + en) // 2
        if cards[mid] > target:
            en = mid

        else:
            st = mid + 1

    return st


# print(cards)

for m in m_list :

    # 젤 빠른 방법

    #left_pos = bisect.bisect_left(cards, m)
    #right_pos = bisect.bisect_right(cards, m)

    #print(right_pos - left_pos, end=" ")

    # 정석 풀이

    l_idx = lower_idx(m)
    u_idx = upper_idx(m)

    print(u_idx - l_idx, end=" ")