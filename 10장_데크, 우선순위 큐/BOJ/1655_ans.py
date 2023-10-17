# 개념을 보고 외우는 게 나을듯 -> 이런 유형 처음
# https://hongcoding.tistory.com/93
# 최대힙, 최소힙 둘 다 이용! -> "중간" 값을 구하기 때문

import sys, heapq

input = sys.stdin.readline

n = int(input())

leftHeap = [] # 중간값보다 작은 값들 -> 최대힙으로 구성
rightHeap = [] # 중간값보다 큰 값들 ->최소힙으로 구성 
# -> leftHeap의 첫 원소를 중간값으로 만들기 가능

for i in range(n) :
    num = int(input())
    
    if len(leftHeap) == len(rightHeap) :
        heapq.heappush(leftHeap, -num)
        
    else :
        heapq.heappush(rightHeap, num)
        
    if rightHeap and rightHeap[0] < -leftHeap[0] : # rightHeap에 leftHeap 보다 작은 값을 넣게 된다면,
        # rightHeap에 중간값보다 큰 원소가 들어가게 되므로,
        # leftHeap의 첫 원소와 rightHeap의 첫 원소를 교체하여 균형 유지
        leftValue = heapq.heappop(leftHeap)
        rightValue = heapq.heappop(rightHeap)

        heapq.heappush(leftHeap, -rightValue)
        heapq.heappush(rightHeap, -leftValue)

    print(-leftHeap[0]) 
