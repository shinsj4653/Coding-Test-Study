# 1 10 -> 방문 처리해야 맞음
# 17 5 -> 왔던 경로를 다시 방문해야하기 때문에 방문 처리 안해줘야 맞음

# 맞왜틀
# 정답
# 핵심로직
# 1. bfs 구조 -> 수빈이랑 동생이 같이 가는 경우 체크
# 2. +1, -1 -> 수빈이가 먼저 왔을 때 동생이랑 홀, 짝 맞아서 만나는 경우

# 보통 상태값 2개 -> 2차원 배열
# 하지만 50만 * 50만 너무 큼
# -> 수빈이가 홀짝인지만 체크하면 됨
# -> 그리고 flood fill 방식 활용해서 풀면 됨


from collections import deque, defaultdict
import sys

input = sys.stdin.readline

n, k = map(int, input().split())

MAX = 500000
#visited = defaultdict(list)
visited = [[0 for _ in range(MAX + 4)] for _ in range(2)]
ok, turn = False, 1

if n == k :
    print(0)
else :
    visited[0][n] = 1
    q = deque([n])

    while q :
        k += turn
        if k > MAX : break

        if visited[turn % 2][k] :
            # 수빈이가 홀수초(3), 혹은 짝수초(2)에 특정지점에 왔었다면
            # 동생이 홀수초(5), 혹은 짝수초(4)에 그 지점에서 만날 수 있다
            # -> 수빈이가 +1, -1 하면 되니까 (2번의 연산)
            ok = True
            break

        qSize = len(q)
        # flood fill
        # 한 턴을 기준으로 단계별로 탐색

        # 3 -> 9 -> 27 ...
        for i in range(qSize) :
            x = q.popleft()
            for nx in [x + 1, x - 1, x * 2] :
                if 0 <= nx <= MAX and not visited[turn % 2][nx] :
                    visited[turn % 2][nx] = visited[(turn + 1) % 2][x] + 1
                    q.append(nx)
                    if nx == k :
                        ok = True
                        break

            if ok:
                break

        if ok :
            break

        turn += 1

    if ok :
        print(turn)

    else :
        print(-1)



