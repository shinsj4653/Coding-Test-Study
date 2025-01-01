# https://kjhoon0330.tistory.com/entry/BOJ-2075-N%EB%B2%88%EC%A7%B8-%ED%81%B0-%EC%88%98-Python
# 큐에 넣는 것 만으로도 메모리 잡아먹는다는 사실 간과..
# 길이 체크하면서 넣어주면 된다.

# 우선순위 큐 개념 복습
# https://www.daleseo.com/python-priority-queue/
# heapq 모듈
# https://www.daleseo.com/python-heapq/

import sys, heapq

input = sys.stdin.readline

n = int(input())
q = []

# 길이가 n인 만큼 우선순위 큐를 돌린다
for i in range(n) :
    for num in map(int, input().split()) :
        if len(q) < n :
            heapq.heappush(q, num)
        else :
            if num > q[0] :
                heapq.heappop(q)
                heapq.heappush(q, num)

print(q[0])