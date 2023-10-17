from itertools import permutations

n = int(input())
k = int(input())

cards = []

for i in range(n) :
    cards.append(input().strip())

print(len(set("".join(i) for i in permutations(cards, k))))