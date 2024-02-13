# 맞왜틀
# 짝짓기로 발상해보기
# -> 거의 90%는 짝짓기 문제는 스택으로 풀림
# 오큰수와 나머지 수를 짝짓기

# 하지만, 그 전에 무식하게 풀 수 있는지 체크
# -> 이건 이미 처음 문제 풀때 파악 완료

import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [-1 for _ in range(n)]
prev = arr[0] # 이전
st = deque()

# 1. 오큰수 : 오른쪽으로 탐색
# 오큰수 결정되지 않으면 담아놓다가..
# 2. 담아놓고 생각
# 오큰수 결정되면 그 때 결과값 배열에 오큰수 담아두기

for i in range(n) :
    while st and arr[st[-1]] < arr[i] :
        dp[st[-1]] = arr[i]
        st.pop()
    st.append(i)

print(*dp)