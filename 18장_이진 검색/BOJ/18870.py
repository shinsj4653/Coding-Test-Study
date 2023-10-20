# set 으로 중복 제거하고 다시 list 화 하는 방법 맞을까??

import sys, bisect
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().rstrip().split()))

sorted_list = list(set(sorted(n_list)))
sorted_list.sort()

#print(sorted_list)

for num in n_list :
    print(bisect.bisect_left(sorted_list, num), end=" ")

