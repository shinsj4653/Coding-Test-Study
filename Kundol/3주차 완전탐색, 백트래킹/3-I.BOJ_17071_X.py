# 1 10 -> 방문 처리해야 맞음
# 17 5 -> 왔던 경로를 다시 방문해야하기 때문에 방문 처리 안해줘야 맞음

#


from collections import deque, defaultdict
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

limit = 500000
MAX = 10 ** 6
#visited = defaultdict(list)
visited = [0 for _ in range(MAX)]

visited[n] = 1
speed = 1

q = deque([(n, k, 1)])
final_k = -1
over_limit = False

if n == k :
    print(0)
else :

    while q :

        now, kk, speed = q.popleft()
        #print('now: ', now)
        #print('k: ', kk)


        if now == kk :
            #print('same!')
            final_k = now
            break

        prev = visited[now] # 이전 값을 뺀 다음

        for next in [now - 1, now + 1, now * 2] :
            if 0 <= next < MAX and visited[next] < visited[now] :
                #print('next: ', next)
                visited[next] = visited[now] + 1
                #print('visited: ', visited[:32])
                next_k = kk + speed
                q.append((next, next_k, speed + 1))

            elif next > limit:
                over_limit = True
                break

        if over_limit: break

    if final_k == -1 or over_limit :
        print(-1)
    else :
        ret = visited[final_k]
        print(ret - 1)


# 1              10
# 0 2 2        11

# (-1 1 0) (1 3 4) (1 3 4)       13

#                       (  8)                 16
#                                  16     20
#                                  32         25
#                                   31    31