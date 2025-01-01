import sys
from collections import deque

input = sys.stdin.readline

# n : 수빈, k : 동생
n, k = map(int, input().split())

#[0, 0, 0, 1, 5, 1 0 0 2 1 2 0 0 0 0 0 17, 0 0 2]

q = deque([(n, 0)])
answer = 0
road = [0] * (k + 1)
road[n] = n
road[k] = k

def bfs() :
    global answer

    while q :
        idx, time = q.popleft()

        if idx - 1 >= 0:
            if road[idx - 1] == k :
                print(time + 1)
                return
            q.append((idx - 1, time + 1))

        if idx + 1 <= len(road) - 1 :
            if road[idx + 1] == k :
                print(time + 1)
                return
            q.append((idx + 1, time + 1))

        if 2 * idx <= len(road) - 1 :
            if road[2 * idx] == k :
                print(time + 1)
                return
            q.append((2 * idx, time + 1))

bfs()