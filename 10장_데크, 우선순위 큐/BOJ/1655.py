import sys, heapq

input = sys.stdin.readline

n = int(input())

queue = []

for i in range(n) :
    heapq.heappush(queue, int(input()))
    print(queue)

