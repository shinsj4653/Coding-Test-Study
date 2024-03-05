# 정답
# 완탐은 3억 이라 안되지 않나?? 아마 스택으로 풀어야 할 것 같은데

# 최대범위로 시간 복잡도를 얼추 잡은 다음 문제 해결 방법 모색

# 외워야 하는 숫자
# 10! -> 362만 정도다
# 2^10 -> 1024
# 3^10 -> 6만 정도

# 10! 이여서 완탐가능

# 필요한 로직
# 1. 2 < 1 (x) 2 < 3 (o) -> 크기 비교 로직
# 2. 방문 여부 체크
# 3. 최대 최소 체크

# 주의
# 문자열 대소비교 -> size가 같아야 비교 해야한다
# 23 과 123 -> 23이 더 커지기 때문

# 재귀 dfs로

n = int(input())
a = input().split()
ret = []
check = [0 for i in range(10)]

def good(x, y, op) :
    if x < y and op == "<" : return True
    if x > y and op == ">" : return True
    return False

def go(idx, num) :
    if idx == n + 1 :
        ret.append(num)
        return

    for i in range(10) :
        if check[i] :
            continue

        if idx == 0 or good(num[idx - 1], str(i), a[idx - 1]) :
            check[i] = 1
            go(idx + 1, num + str(i))
            check[i] = 0

go(0, "")
ret.sort(reverse=True)
print(ret[0])
print(ret[len(ret) - 1])