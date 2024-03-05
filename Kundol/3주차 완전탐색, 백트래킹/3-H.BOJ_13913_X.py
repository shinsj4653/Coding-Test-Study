# 숫자 변경 과정 기록
# -> 이거야말로 재귀여야 하지 않나??
# -> 왜냐하면 그냥 기록이 아니라 순서대로 기록을 해야하기 때문..

# visited를 배열이 아닌 map으로?
# -> 맞왜틀


from collections import deque, defaultdict
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

if n == k:
    print(0)
    print(1)

else :
    MAX = 10 ** 5
    # visited = [0 for _ in range(MAX + 1)]
    visited = defaultdict(list)
    visited[n] = [n]
    cnt = [0 for _ in range(MAX + 1)]
    cnt[n] = 1
    q = deque([n])

    while q :
        now = q.popleft()
        for next in [now + 1, now - 1, now * 2] :
            if 0 <= next <= MAX :
                #print('len(visited[next] : ', len(visited[next]))
                if len(visited[next]) == 0 :
                    q.append(next)
                    visited[next] = [next] # 초기 방문
                    visited[next].extend(visited[now]) # 지금까지의 경로들 extend

                    #print('visited[now] : ', visited[now])
                    #print('visited[next] : ', visited[next])

                # elif visited[next] == visited[now] + 1 :
                #     print('cnt[now] : ', cnt[now])
                #     cnt[next] += cnt[now]

    #print(visited)
    #print(cnt)

    print(len(visited[k]) - 1)
    print(*reversed(visited[k]))

