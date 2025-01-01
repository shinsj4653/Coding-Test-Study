import sys, heapq

input = sys.stdin.readline

n = int(input())
q = []

# 길이가 n인 만큼 우선순위 큐를 돌린다
for i in range(n) :
    for num in map(int, input().split()) :
        heapq.heappush(q, -num)

ans = 0
for i in range(n) :
    ans = heapq.heappop(q)

print(-ans)