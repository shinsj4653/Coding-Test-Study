# & -> and: 모두 1인 부분 제외하고 0
# | -> or : 모두 0인 부분 제외하고 1

# a << n : a * 2^n
# a >> n : a // 2^n

# 실전에서 활용될 때는 주로 a값이 1

# ^ -> XOR: 같 0 다 1

# ~ -> one's completion: 1의 보수
# 즉, 비트 반전

# ~value = -(value + 1)
# -> 왜 그럴까
# -> 음수 표현 : 비트 반전하여 + 1
# 따라서, -a = ~a + 1


def dfs(queen, row, n):
    count = 0
    if n == row:
        return 1
    for col in range(n):
        queen[row] = col
        for i in range(row):
            if queen[i] == queen[row]:
                break
            if abs(queen[i]-queen[row]) == row - i:
                break
        else:
            count += dfs(queen, row + 1, n)
    return count
def solution(n):
    return dfs([0]*n, 0, n)

solution(4)