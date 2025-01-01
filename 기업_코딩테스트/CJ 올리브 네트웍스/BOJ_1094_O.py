# 64
#    32
#    16 16
#       8  8
        #  4  4
        #     2  2
         #        1  1

# 23

# 16 + 4 + 2 + 1

from collections import deque

x = int(input())

memo = {} # key값을 만들기 위한 막대기 총 갯수
li = deque()

def dp(n, l) :

    if sum(l) == x :
        return

    if n > x :
        dp(n // 2, l)

    else :
        if sum(l) + n <= x :
            l.append(n)
        dp(n // 2, l)

    return

dp(64, li)

print(len(li))