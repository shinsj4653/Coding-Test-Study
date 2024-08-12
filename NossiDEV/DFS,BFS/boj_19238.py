from collections import deque
import sys

input = sys.stdin.readline
#✅ 입력 형식에 맞춰서 입력값을 받는다.
n, m, fuel = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
tr, tc = map(int,input().split())
tr -= 1
tc -= 1
#✅ 승객의 출발지와 도착지를 해시테이블에 저장한다.
passenger = {}
for i in range(m):
    pr, pc, pdr, pdc = list(map(int, input().split()))
    passenger[(pr-1, pc-1)] = (pdr-1, pdc-1)

answer = 0

def in_range(next_r, next_c) :
    return 0 <= next_r < n and 0 <= next_c < n

def pickup(tr, tc) :
    q = deque([[tr, tc, 0]])
    v = {(tr, tc)}
    candidate = []
    min_distance = 1000000

    while q :
        cur_r, cur_c, cur_d = q.popleft()

        if cur_d > min_distance :
            break

        if (cur_r, cur_c) in passenger :
            candidate.append((cur_r, cur_c))
            min_distance = cur_d

        for dr, dc in [[-1,0],[1,0],[0,-1],[0,1]]:
            next_r, next_c, next_d = cur_r + dr, cur_c + dc, cur_d + 1
            if (next_r, next_c) in v :
                continue
            if in_range(next_r, next_c) and board[next_r][next_c] != 1 :
                q.append([next_r, next_c, next_d])
                v.add((next_r, next_c))

    return candidate, min_distance

def go_dest(tr, tc) :
    pdr, pdc = passenger[(tr, tc)]
    del passenger[(tr, tc)]
    q = deque([[tr, tc, 0]])
    v = {(tr, tc)}

    while q:
        cur_r, cur_c, cur_d = q.popleft()
        if cur_r == pdr and cur_c == pdc:
            return cur_r, cur_c, cur_d
        for dr, dc in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            next_r, next_c, next_d = cur_r + dr, cur_c + dc, cur_d + 1
            if (next_r, next_c) in v:
                continue
            if in_range(next_r, next_c) and board[next_r][next_c] != 1:
                q.append([next_r, next_c, next_d])
                v.add((next_r, next_c))

    return pdr, pdc, 10000000

while fuel > 0 and len(passenger) != 0 :

    cand, used_fuel = pickup(tr, tc)

    if used_fuel > fuel or len(cand) == 0:
        answer = -1
        break

    tr, tc = sorted(cand)[0]

    fuel -= used_fuel

    pdr, pdc, used_fuel = go_dest(tr, tc)
    if used_fuel > fuel :
        answer = -1
        break

    fuel += used_fuel
    tr, tc = pdr, pdc

if answer == -1 :
    print(-1)

else :
    print(fuel)
