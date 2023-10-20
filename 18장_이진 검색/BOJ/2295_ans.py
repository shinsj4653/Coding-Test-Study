# 3개의 숫자 중, 2개짜리 조합에 대한 배열
# 그리고, 정답과 나머지 숫자의 차이가 윗 배열에 존재하는지 체크!!

# [ 핵심 ]
# 먼가 2개를 먼저 묶고, 나머지에 대한 요소를 이분탐색하여 시간복잡도 낮추는 아이디어

import bisect
import sys
input = sys.stdin.readline

n = int(input())
nums = []

for i in range(n) :
    nums.append(int(input()))

nums.sort()

two = []

for i in range(n) :
    for j in range(n) :
        two.append(nums[i] + nums[j])

two.sort()

for i in range(n - 1, 0, -1) :
    for j in range(i) :
        if bisect.bisect_left(two, (nums[i] - nums[j])) :
            print(nums[i])
            exit()