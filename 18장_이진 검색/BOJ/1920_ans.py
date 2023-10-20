# bisect 써서 풀면 안되나??


import sys, bisect
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().rstrip().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().rstrip().split()))

def binary_search(target) :
    st = 0
    en = n - 1

    while st <= en :
        mid = (st + en) // 2
        if n_list[mid] < target :
            st = mid + 1

        elif n_list[mid] > target :
            en = mid - 1

        else :
            return 1

    return 0

for m in m_list :
    print(binary_search(m))

