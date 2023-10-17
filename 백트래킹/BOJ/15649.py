import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0 for _ in range(m)]
is_used = [False for _ in range(n + 1)]

def func(k) :
    if k == m :
        for i in range(m) :
            print(arr[i], end = " ")
        print()
        return

    for i in range(1, n + 1) :
        if not is_used[i] :
            arr[k] = i
            is_used[i] = True
            func(k + 1)
            is_used[i] = False

func(0)