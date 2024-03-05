# 1차원 배열 bfs
# 5 17
# 4 8 16 17
# 10 9 18 17
# -1 +1 *2

# 횟수 key, 경로 수 value -> dict 활용

# n이 k의 배수가 되는 순간 무조건 *2가 이득

from collections import defaultdict
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

n, k = map(int, input().split())
dic = defaultdict(int)

min_time = 10e9

def find(n, k, time) :
    global min_time

    if time > min_time: # 이미 최솟값 정해졌는데 그보다 오래걸린다면 볼 필요 없다
        return

    if n < 0 or n > 10 ** 5 : #
        return

    if n == k :
        min_time = min(min_time, time)
        dic[min_time] += 1
        return

    if n - 1 != 0 and (k == n - 1 or k % (n - 1) == 0 or k + 1 % (n - 1) == 0 or k - 1 % (n - 1) == 0) :
        n -= 1
        find(n, k, time + 1)
    elif n + 1 != 0 and (k == n + 1 or k % (n + 1) == 0 or k + 1 % (n + 1) == 0 or k - 1 % (n + 1) == 0) :
        n += 1
        find(n, k, time + 1)
    elif n != 0 and (k % n == 0) :
        n *= 2
        find(n, k, time + 1)
    else :
        find(n - 1, k, time + 1)
        find(n + 1, k, time + 1)
        find(n * 2, k, time + 1)

find(n, k,0)

print(min_time)
print(dic[min_time])

##-1 +1 *2
# 3   3  3 9
# 333 333  333 27
# 333333333 27 81