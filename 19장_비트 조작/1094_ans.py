# 왜 이해가 안가냐..
# 23 -> 16 막대기 붙이면 7 남음
# 이 7을 4 2 1 로 만들기 가능!

import sys
input = sys.stdin.readline
X = int(input())
# 2  23
#   11   1
#    5   1
#    2   1
#    1   0
#    0   1
# -> 2진법!

print(str(bin(X)).count('1'))


