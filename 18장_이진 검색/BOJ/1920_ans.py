# bisect 써서 풀면 안되나??


import sys, bisect
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().rstrip().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().rstrip().split()))

for num in m_list :
    print(bisect.bisect_left(n_list, num))
