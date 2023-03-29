import sys

# 여러줄 입력받는 상황에서는 input이 시간초과가 날 수 있다.
input = sys.stdin.readline

k = int(input())

size = 1
cnt = 0

while size < k:
    # << 연산자 -> 2씩
    size = size << 1
result1 = size

while k > 0 :
    if k >= size :
        k -= size
    else :
        size //= 2
        cnt += 1

print(result1, cnt)