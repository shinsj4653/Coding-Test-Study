from collections import deque

n = int(input())
card = deque()
for i in range(1, n + 1) :
    card.append(i)

while len(card) > 1 :
    card.popleft()
    if len(card) == 1 :
        break
    else :
        top = card.popleft()
        card.append(top)

print(card[0])