
cnt = 0
def solve(N) :
    global cnt
    cnt += 1
    if N == 0 :
        return
    for i in range(3) :
        solve(N - 1)


    return

N = int(input())
solve(N)
print(cnt)