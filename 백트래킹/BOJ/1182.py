import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

is_used = [False for _ in range(len(arr))]

print(arr)
print(is_used)

answer = 0

def func(cur_sum) :
    global answer

    if cur_sum == s :
        answer += 1
        return

    


func(0)