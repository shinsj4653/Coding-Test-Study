# DP는 상태값이 중요
# 중요한 상태값 3가지 : t, w, idx(자두 위치)
# 기저사례, 메모이제이션, 로직, 초기화

dp = [[[0 for _ in range(34)] for _ in range(2)] for _ in range(1004)]

# 초기화
n, m = map(int, input().split()) # 초의 값, 몇 번 움직일 수 있나
b = [0 for i in range(1005)]

def go(idx, tree, cnt) :
    # 기저 사례
    if cnt < 0 : return -1e9
    if idx == n :
        return 0 if cnt == 0 else -1e9

    # 메모이제이션
    ret = dp[idx][tree][cnt]
    if -ret :
        return ret

    # 로직
    return ret = max(go(idx + 1, tree^1, cnt - 1), go(idx + 1, tree, cnt)) + (tree == b[idx] - 1)





for i in range(n) :
    b[i] = int(input())

print(max(go(0, 1, m - 1), go(0, 0, m)))
