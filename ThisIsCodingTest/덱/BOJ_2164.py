# https://covenant.tistory.com/143
# rotate 개념 외워두기!

#

from collections import deque

N = int(input())
cards = deque([i for i in range(1, N + 1)])

while len(cards) > 1 :
    cards.popleft()
    cards.rotate(-1)
    print(cards)

print(cards[0])

